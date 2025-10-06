from django.urls import path,include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name="index"),
    path('profile/',views.profile,name="profile"),
    path('bookmark/<int:id>',views.bookmark,name="bookmark"),
    path('delete_bookmark/<int:id>',views.delete_bookmark,name="delete_bookmark"),
    path('reserve/',views.reserve,name="reserve"),
    path("payment-success/", views.payment_success, name="payment_success"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)