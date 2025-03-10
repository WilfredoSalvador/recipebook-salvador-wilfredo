"""Modules importing the Profile model for the Admin Panel."""
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Profile

class ProfileInLine(admin.StackedInline):
    """
    An in line admin for Profile.
    """
    model=Profile
    can_delete=False

class UserAdmin(BaseUserAdmin):
    """
    An admin panel for Users.
    """
    inlines = [ProfileInLine,]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
