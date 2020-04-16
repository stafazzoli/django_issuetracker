from django.contrib import admin
from django.contrib.auth.models import User
from . import models


# Register your models here.
admin.site.register(models.Profile)


# Adding Profile to User page
# class ProfileInLine(admin.StackedInline):
#     model = models.Profile
#
#
# class UserAdmin(admin.ModelAdmin):
#     inlines = [
#         ProfileInLine,
#     ]
#
#
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)


