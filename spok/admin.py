from django.contrib import admin
from django.contrib.auth.models import User
from .models import * 
admin.site.register(Sala)
admin.site.register(User)
# Register your models here.
