
"""
فیلد usable_password را گذاشته‌ای، اما مدل/فرم تو آن را نمی‌شناسد.
چرا این اتفاق افتاده؟
از Django 5.1 به بعد، فیلدی به نام usable_password وارد رفتار فرم‌های ساخت یوزر در ادمین شده.
اگر تو فرم سفارشی بنویسی:

CustomUserCreationForm(UserCreationForm)
ولی در admin.py هنوز add_fieldsets قدیمی یا کپی‌شده از UserAdmin را داشته باشی، بین فرم و ادمین ناسازگاری پیش می‌آید.
راه‌حل‌ها
راه‌حل 1: اگر usable_password نمی‌خواهی
در admin.py آن را از add_fieldsets حذف کن.
مثلاً:
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
	
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username' , 'email', 'age' , 'is_staff']
    fieldsets = (
        (None, {"fields": ("email", "username", "age", "password")}),
        ("Permissions", {
            "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")
        }),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "age", "password1", "password2"),
        }),
    )
# admin.site.register(CustomUser , CustomUserAdmin) چون بصورت دکوراتور بالای کلاس اصلی نوشته شده دیگه اینجا نمیشه بنویسیم پس کامنتش میکنیم


