from django.db import models
from django.contrib.auth.models import AbstractUser  #, AbstractBaseUser

# Create your models here.

'MY Custom user model '
""" اینکار باعث میشه که جنگو از مدل یوزر خودش  که همون (auth.modeluser) هست استفاده نکنه و مستقیم بره
سراغ مدل یوزری که از اپ accounts پروژه که توسط دولوپر ایجاد میشه بهره بگیره"""
# AUTH_USER_MODEL = "accounts.CustomUser" که در settings.py موجودش کردیم
class CustomUser(AbstractUser): # AbstractUser درون خودش --> شامل --> username, lastname , email , password ,... میباشد
    # nat_id : National ID : کد ملی
    age = models.PositiveIntegerField(null = True , blank = True)
    


    
