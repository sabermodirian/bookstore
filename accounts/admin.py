from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from accounts.forms import CustomUserChangeForm , CustomUserCreationForm

# Register your models here.

class CustoUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser
	

admin.site.register(CustomUser , CustoUserAdmin)


