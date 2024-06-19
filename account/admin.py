from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'phone_number', 'is_superuser']
    search_fields = ['username', 'first_name', 'last_name', 'phone_number']
    fieldsets = [
        (None, {'fields': ['email', 'first_name', 'last_name', 'phone_number', 'date_joined', 'last_login']}),
        ('Администратор', {'fields': ['is_superuser']}),
    ]
