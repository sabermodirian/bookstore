# AdminUserCreationForm --> SignUp
# UserChangeForm  --> Admin

"""
با توجه به اینکه Django شما 6.1.1 است، بهتر است برای فرم افزودن کاربر در پنل ادمین از AdminUserCreationForm استفاده کنیم؛ چون فیلد usable_password را پشتیبانی می‌کند.

فرض می‌کنم مدل CustomUser از AbstractUser ارث‌بری کرده و فقط فیلد age به آن اضافه شده است.
"""
from django.contrib.auth.forms import (
    AdminUserCreationForm,
    UserChangeForm,
)

from .models import CustomUser


class CustomUserCreationForm(AdminUserCreationForm):
    class Meta(AdminUserCreationForm.Meta):
        model = CustomUser
        # fields = AdminUserCreationForm.Meta.fields + ("age",)
        fields = ('username' ,'last_name' ,'age' , 'email' ,)
	    

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username','last_name', 'age' , 'email' ,)

'''
نکته مهم این قسمت است:

AdminUserCreationForm
در نسخه‌های جدید Django این فرم مخصوص ساخت کاربر در پنل ادمین است و فیلد usable_password را می‌شناسد.
'''
