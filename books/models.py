from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# todo چه کاستوم یوزر باشد و چه آوث یوزر باشد. به جنگو میگیم خودت برو مدل یوزر اصلی رو پیدا بکن

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length = 200 , verbose_name = 'Title')
	author = models.CharField(max_length = 200 , verbose_name = 'Author')
	description = models.TextField(verbose_name = 'Description')
	price = models.DecimalField(decimal_places = 3 , max_digits = 7 , verbose_name = 'Price')
	#decimal_places : تعداداعشار , max_digits : تعدادکل ارقام
	
	bk_cover = models.ImageField(upload_to = 'covers/', blank = True , verbose_name = 'Book Cover') #تصاویر جلد کتابها را در این مسیر ذخیره کن
	
	
	def __str__(self):
		return f'{self.title} : اثری ماندگار از نویسنده :  {self.author} '
	
	def get_absolute_url(self):
		"""هر شیئی ازین کلاس book ساخته شد برایش یک url در نظر بگیر"""
		return reverse('books:book_details' , kwargs={'pk': self.pk})

class Comment(models.Model):
	user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE) # FK به یوزر مدل
	book = models.ForeignKey(Book , on_delete = models.CASCADE, related_name = 'cmnts_rel') # FK به مدل کتاب BOOK در همینجا(بالا)
	text = models.TextField(verbose_name = 'Comment_Txt')
	created_at = models.DateTimeField(auto_now = True , verbose_name = 'Created at ')
	
	def __str__(self):
		return f'{self.user} writed: this {self.text} for  this: {self.book}'