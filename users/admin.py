from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User, FinancialRecord

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'role', 'is_active', 'is_staff')
    list_filter = ('role', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Role Management', {'fields': ('role',)}),
    )

admin.site.register(FinancialRecord)