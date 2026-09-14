from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import  generic # CBV :Class Base View

from books.models import Book


# Create your views here.

# class BooklistView(generic.ListView):
# 	model = Book
# 	template_name = 'books/book_list.html'
# 	context_object_name = 'books'
#
#
# class BookDetailsView(generic.DetailView):
# 	model = Book
# 	template_name = 'books/book_details.html'
	
class BookCreateView(generic.CreateView):
	model = Book
	fields = ['title' , 'author' , 'description' , 'price']
	template_name =  'books/book_create.html'
	# success_url = reverse_lazy('books:book_details', kwargs={'pk': self.object.pk} )
	# #
	def get_success_url(self) :
	 	return reverse_lazy('books:book_details' , kwargs = {'pk' : self.object.pk})
	
	نکته
	ای
	مهم: اگر
	بخواهی
	از
	success_url
	استفاده
	کنی
	success_url
	فقط
	برای
	URLهای
	ثابت
	مناسب
	است؛ مثلاً:
	
	content_copy
	python
	
	note_add
	ویرایش
	با
	Canvas
	from django.urls import reverse_lazy
	
	class BookCreateView(generic.CreateView) :
		model = Book
		fields = ['title' , 'author' , 'description' , 'price']
		template_name = 'books/book_create.html'
		success_url = reverse_lazy('books:book_list')
	
	چون
	book_list
	به
	pk
	نیاز
	ندارد:
	
	
	path('' , BooklistView.as_view() , name = 'book_list')
	اما
	book_details
	نیاز
	دارد:
	
	path('<int:pk>/' , BookDetailsView.as_view() , name = 'book_details')
	پس
	این
	درست
	نیست:
	
	success_url = reverse_lazy('books:book_details')
	و
	این
	هم
	درست
	نیست:
	
	success_url = reverse_lazy(
		'books:book_details' ,
		kwargs = {'pk' : self.object.pk}
	)
	جمع‌بندی
	کوتاه
	
	
	کد
	زمان
	اجرا
	نتیجه
	success_url = reverse_lazy(...)
	هنگام
	تعریف
	کلاس
	self.object
	وجود
	ندارد
	get_success_url(self)
	بعد
	از
	ذخیرهٔ
	فرم
	self.object.pk
	وجود
	دارد
	success_url = reverse_lazy('books:book_list')
	URL
	ثابت
	صحیح
	get_success_url()
	برای
	book_details
	URL
	پویا
	با
	pk
	صحیح
	نسخهٔ
	نهایی
	پیشنهادی:
	
	
	class BookCreateView(generic.CreateView) :
		model = Book
		fields = ['title' , 'author' , 'description' , 'price']
		template_name = 'books/book_create.html'
		
		def get_success_url(self) :
			return reverse(
				'books:book_details' ,
				kwargs = {'pk' : self.object.pk}
			)
	
	فقط
	یادت
	باشد
	import هم
	داشته
	باشی:
	
	
	from django.urls import reverse


	

