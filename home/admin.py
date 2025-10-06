from django.contrib import admin
from .models import Category,Item,Bookmark,Profile,Reservation

# Register your models here.
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Bookmark)
admin.site.register(Profile)
admin.site.register(Reservation)