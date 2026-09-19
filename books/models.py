from django.db import models
from django.urls import reverse


# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length = 200 , verbose_name = 'Title')
	author = models.CharField(max_length = 200 , verbose_name = 'Author')
	description = models.TextField(verbose_name = 'Description')
	price = models.DecimalField(decimal_places = 3 , max_digits = 7 , verbose_name = 'Price')
	#decimal_places : تعداداعشار , max_digits : تعدادکل ارقام
	
	bk_cover = models.ImageField(upload_to = 'covers/', blank = True) #تصاویر جلد کتابها را در این مسیر ذخیره کن
	
	
	def __str__(self):
		return f'{self.title} : اثری ماندگار از نویسنده :  {self.author} '
	
	def get_absolute_url(self):
		"""هر شیئی ازین کلاس book ساخته شد برایش یک url در نظر بگیر"""
		return reverse('books:book_details' , kwargs={'pk': self.pk})
