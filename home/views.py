from django.shortcuts import render, redirect, HttpResponse
from .models import Category, Item, Bookmark, Profile, Reservation
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from allauth.account.signals import user_signed_up

import razorpay

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))


def send_welcome_email(user):
    subject = "🍴 Welcome to Your Restaurant!"
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = user.email

    context = {
        "user": user,
    }

    html_content = render_to_string('emails/welcome_email.html', context)
    msg = EmailMultiAlternatives(subject, html_content, from_email, [to_email])
    msg.send()

@receiver(user_signed_up)
def send_email_on_signup(request, user, **kwargs):
    send_welcome_email(user)


# Create your views here.
def index(request):
    categories = Category.objects.all()
    items = Item.objects.all()
    bookmarked_items = None
    if request.user.is_authenticated:
        bookmarked_items = request.user.bookmark_set.values_list("item_id", flat=True)
    context = {
        "categories": categories,
        "items": items,
        "bookmarked_items": bookmarked_items,
    }
    return render(request, "home/index.html", context=context)


@login_required
def bookmark(request, id):
    item = Item.objects.get(id=id)
    user = request.user
    bookmark = Bookmark(user=user, item=item)
    bookmark.save()
    return redirect("/#menu")


@login_required
def delete_bookmark(request, id):
    item = Item.objects.get(id=id)
    bookmark = Bookmark.objects.filter(user=request.user, item=item)
    bookmark.delete()
    return redirect("/#menu")


@login_required
def profile(request):
    if request.method == "POST":
        if "profile_pic" in request.FILES:
            profile = Profile.objects.get(user=request.user)
            profile.profile_pic = request.FILES["profile_pic"]
            profile.save()
            return redirect("profile")
    bookmarks = Bookmark.objects.filter(user=request.user)
    profile = Profile.objects.get(user=request.user)
    reservations = Reservation.objects.filter(user=request.user)
    return render(
        request,
        "home/user_profile.html",
        context={
            "bookmarks": bookmarks,
            "profile": profile,
            "reservations": reservations,
        },
    )


@login_required
def reserve(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user

            # Here i am creating razorpay payment link where user will be redirected and will pay

            data = {
                "amount": 200 * 100,  # in paise
                "currency": "INR",
                "accept_partial": False,
                "description": f"We look forward to welcoming you! To ensure all our guests have the best experience, we require a booking credit of ₹150 per person to confirm your reservation.This is not an extra fee. The full amount of your booking credit will be deducted from your final bill on the day of your visit.",
                "customer": {
                    "name": request.user.username,
                    "email": request.user.email,
                },
                "notify": {"sms": False, "email": True},
                "reminder_enable": True,
                "callback_url": request.build_absolute_uri("/payment-success/"),
                "callback_method": "get",
            }

            payment_link = client.payment_link.create(data)

            reservation.razorpay_payment_link_id = payment_link["id"]
            reservation.save()

            return redirect(payment_link["short_url"])
    return render(request, "home/reservation.html")


def payment_success(request):
    payment_id = request.GET.get("razorpay_payment_id")
    link_id = request.GET.get("razorpay_payment_link_id")

    try:
        # Fetch payment details
        payment = client.payment.fetch(payment_id)
        reservation = Reservation.objects.get(razorpay_payment_link_id=link_id)
        if payment["status"] == "captured":
            reservation.razorpay_payment_id = payment_id
            reservation.status = "Confirmed"
            reservation.save()
            return redirect("profile")
        else:
            reservation.status = "failed"
            reservation.save()
            return HttpResponse("Payment Failed!")
    except Exception:
        return HttpResponse("Payment verification failed.")


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
