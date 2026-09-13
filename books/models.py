from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length = 200)
	author = models.CharField(max_length = 200)
	description = models.TextField()
	price = models.DecimalField(decimal_places = 3 , max_digits = 7)
	#decimal_places : تعداداعشار , max_digits : تعدادکل ارقام
	def __str__(self):
		return self.title
