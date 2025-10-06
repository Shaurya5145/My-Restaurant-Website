from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    
class Bookmark(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'item')

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    profile_pic = models.ImageField(default="profile_default.jpg",upload_to="profile_pictures")

class Reservation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    people = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    dietary_restriction = models.TextField()
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
    razorpay_payment_link_id = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=10,default="Processing")
