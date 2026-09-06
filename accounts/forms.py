# UserCreationForm --> SignUp
# UserChangeForm  --> Admin

from django.contrib.auth.forms import UserChangeForm , UserCreationForm

from .models import CustomUser  # == from accounts.models  import CustomUser


class CustomUserCreationForm(UserCreationForm):
	'''
	که من ساختم برای یوزرمدلت استفاده کن CustomUser ای فرم جدید لطفا از مدل  '''
	class Meta:
		model = CustomUser
		fields = UserCreationForm.Meta.fields + ('age',)
		
class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = CustomUser
		fields = UserChangeForm.Meta.fields

