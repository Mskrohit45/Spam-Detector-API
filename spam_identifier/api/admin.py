from django.contrib import admin
from .models import User, Contact, SpamFlag

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone_number', 'email', 'is_staff')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'user')

@admin.register(SpamFlag)
class SpamFlagAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'flagged_count')
