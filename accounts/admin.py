
"""
فیلد usable_password را گذاشته‌ای، اما مدل/فرم تو آن را نمی‌شناسد.
چرا این اتفاق افتاده؟
از Django 5.1 به بعد، فیلدی به نام usable_password وارد رفتار فرم‌های ساخت یوزر در ادمین شده.
اگر تو فرم سفارشی بنویسی:

CustomUserCreationForm(UserCreationForm)
ولی در admin.py هنوز add_fieldsets قدیمی یا کپی‌شده از UserAdmin را داشته باشی، بین فرم و ادمین ناسازگاری پیش می‌آید.
راه‌حل‌ها
راه‌حل 2: اگر می‌خواهی منطق جدید Django را نگه داری
باید از فرم مناسب ادمین استفاده کنی:


from django.contrib.auth.forms import AdminUserCreationForm
ولی برای CustomUser معمولاً خیلی وقت‌ها همان روش دستیِ بالا تمیزتر و کنترل‌شده‌تر است.

یک نکته مهم
usable_password فیلد مدل CustomUser نیست؛

بیشتر یک فیلد/رفتار مربوط به فرم ادمین است.

پس اگر در fieldsets یا add_fieldsets آن را گذاشته باشی و فرم تو آن را نداشته باشد، همین خطا را می‌گیری.

جمع‌بندی کوتاه
مشکل اصلی:

در CustomUserAdmin فیلد usable_password هست ولی فرم سفارشی‌ات آن را ندارد.

راه‌حل سریع:

usable_password را از add_fieldsets حذف کن، یا فرم ادمین مناسب Django 5.1+ را استفاده کن.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # فرم ویرایش کاربر
    form = CustomUserChangeForm

    # فرم افزودن کاربر
    add_form = CustomUserCreationForm

    list_display = (
        "username",
        "email",
        "age",
        "is_staff",
        "is_active",
    )

    list_filter = (
        "is_staff",
        "is_active",
        "is_superuser",
    )

    search_fields = (
        "username",
        "email",
        "first_name",
        "last_name",
    )

    ordering = ("username",)

    # فیلدهای صفحه ویرایش کاربر
    fieldsets = UserAdmin.fieldsets + (
        (
            "اطلاعات تکمیلی",
            {
                "fields": ("age",),
            },
        ),
    )

    # فیلدهای صفحه افزودن کاربر
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "اطلاعات تکمیلی",
            {
                "fields": ("age",),
            },
        ),
    )
'''
در این نسخه، add_fieldsets اصلی UserAdmin شامل usable_password است و چون CustomUserCreationForm از AdminUserCreationForm ارث‌بری می‌کند، فرم هم آن را می‌شناسد؛ بنابراین خطای زیر برطرف می‌شود:

Unknown field(s) (usable_password)
'''

# admin.site.register(CustomUser , CustomUserAdmin) چون بصورت دکوراتور بالای کلاس اصلی نوشته شده دیگه اینجا نمیشه بنویسیم پس کامنتش میکنیم

'''
نسخه نهایی هماهنگ این است:

CustomUser
├── CustomUserCreationForm → AdminUserCreationForm
├── CustomUserChangeForm   → UserChangeForm
└── CustomUserAdmin        → UserAdmin
با این ساختار هم age در فرم افزودن و ویرایش نمایش داده می‌شود و هم قابلیت usable_password نسخه جدید Django بدون خطا کار می‌کند.
'''
