from django.contrib import admin

# Register your models here.

from .models import Restaurant, Menu, Vote

admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Vote)