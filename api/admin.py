from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = "Admin Panel Music"
admin.site.register(Room)