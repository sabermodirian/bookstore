# UserCreationForm --> SignUp
# UserChangeForm  --> Admin

from django.contrib.auth.forms import UserChangeForm , UserCreationForm
from .models import CustomUser  # == from accounts.models  import CustomUser


class CustomUserCreationForm(UserCreationForm):
	'''
	که من ساختم برای یوزرمدلت استفاده کن CustomUser ای فرم جدید لطفا از مدل  '''
	# class Meta:
	class Meta(UserCreationForm.Meta): #  در واقع به این شکلست کلاس مت
		model = CustomUser
		fields = UserCreationForm.Meta.fields + ('age',)
		
class CustomUserChangeForm(UserChangeForm):
	# class Meta:
	class Meta(UserChangeForm.Meta):   # در واقع به این شکلست کلاس مت
		model = CustomUser
		# fields = UserChangeForm.Meta.fields  بنابراین در فرم ویرایش دیگر لازم نیست این خط را تکرار کنید


