from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length = 200 , verbose_name = 'Title')
	author = models.CharField(max_length = 200 , verbose_name = 'Author')
	description = models.TextField(verbose_name = 'Description')
	price = models.DecimalField(decimal_places = 3 , max_digits = 7 , verbose_name = 'Price')
	#decimal_places : تعداداعشار , max_digits : تعدادکل ارقام
	def __str__(self):
		return self.title
