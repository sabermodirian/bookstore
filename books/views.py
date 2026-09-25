from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.shortcuts import render , get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import  generic # CBV :Class Base View
#import yor models
from books.models import Book
from books.forms import CommentForm

# Create your views here.
class BooklistView(generic.ListView):
	model = Book
	paginate_by = 5
	template_name = 'books/book_list.html'
	context_object_name = 'books'
#
# class BookDetailsView(generic.DetailView):
# 	model = Book
# 	template_name = 'books/book_details.html'
'''
الگوی PRG یا (Post/Redirect/Get) چیه و چرا گفتم ریدایرکت کنی؟ 🚀
فرض کن کاربر یه کامنت گذاشت: “کتاب خیلی قشنگی بود!” و دکمه «ارسال» رو زد.

❌ سناریوی بدون Redirect (کد فعلی تو):
اگر کاربر بعد از فرستادن کامنت، صفحه‌ی مرورگرش رو رفرش کنه (F5 بزنه)، مرورگر یه پیغام ترسناک بهش میده:

“The page that you’re looking for used information that you entered… Confirm form resubmission?”

کاربر هم بدون اینکه بخونه میزنه Continue؛ و بوم! 💥 کامنتش دوبار توی دیتابیس ثبت میشه! (یا اگه درگاه پرداخت بود، دو بار پول کم می‌شد! 😱).

✅ سناریوی استاندارد با Redirect (الگوی PRG):
جنگوکارای با تجربه میان بعد از اینکه فرم با موفقیت ذخیره شد (save)، کاربر رو ریدایرکت می‌کنن به همون صفحه. اینجوری مرورگر از حالت POST به حالت امنِ GET سوییچ می‌کنه و کاربر ۱۰۰ بارم F5 بزنه، کامنت تکراری ثبت نمیشه!

کد استاندارد و خوشگلش این شکلی میشه:
'''
@login_required
def book_details_view(request, pk):
    book = get_object_or_404(Book, pk=pk) # get book object
    
    book_comments = (book.cmnts_rel
                     .select_related('user')  # برای جلوگیری از کوئری اضافه (N+1) 👌
                     .order_by('-created_at'))
    # get book's comments برای گرفتن کامنتهای هر کتاب با استفاده از related_name
    if request.method == 'POST' :
	    comment_form = CommentForm(request.POST)
	    if comment_form.is_valid() :
		    new_cmnt = comment_form.save(commit = False)
		    new_cmnt.book = book
		    new_cmnt.user = request.user
		    new_cmnt.save()
		    # 🎯 اینجا کاربر رو ریدایرکت می‌کنیم به همین صفحه کتاب:
		    return redirect('books:book_details' , pk = book.pk)  # یا new_cmnt.book.get_absolute_url()
    else :
	    # وقتی درخواست GET هست (کاربر تازه اومده تو صفحه)، یه فرم خالی بهش نشون بده:
	    comment_form = CommentForm()
    
    return render(request ,
                    'books/book_details.html' ,
		                    {
								    'book' : book ,
								    'comment_form' : comment_form ,
	                                'comments' : book_comments ,
		                            }
                  )

	
class BookCreateView(LoginRequiredMixin ,generic.CreateView):
	model = Book
	fields = ['title' , 'author' , 'description' , 'price', 'bk_cover']
	template_name =  'books/book_create.html' #'books/book_create_and_update.html'
	# success_url = reverse_lazy('books:book_details', kwargs={'pk': self.object.pk} )
	# #
	def get_success_url(self) :
	 	return reverse_lazy('books:book_details' , kwargs = {'pk' : self.object.pk})
	
class BookUpdateView( LoginRequiredMixin, UserPassesTestMixin ,generic.UpdateView):
	model = Book
	fields = ['title' , 'author' , 'description' , 'bk_cover']
	template_name =  'books/book_update.html' #'books/book_create_and_update.html'
	
	def test_func(self) :
		"""
		این متد، نقشِ دربونِ سخت‌گیرِ سایت رو بازی می‌کنه! 👮‍♂️

		بررسی می‌کنه که آیا کاربری که درخواست ویرایش داره، همون خالقِ اصلیِ این
		کتاب هست یا نه. اگر یوزرِ لاگین شده صاحبِ اثر باشه، اجازه‌ی ورود به
		ویرایش رو صادر می‌کنه (True)، وگرنه با یه '403 Forbidden' محترمانه
		بیرونش می‌کنه. 🚪🚫

		Returns:
			bool: True اگر کاربر صاحب کتاب باشد، در غیر این صورت False.
		"""
		book_obj = self.get_object()  #  گرفتن و داشتن آبجکت کتابی را که در این کلاس آپدیت درحال ویرایش آن هستیم
		# گرفتن آبجکت کتابی که قراره زیر تیغِ ویرایش بره!
		
		return book_obj.user == self.request.user # اگر یوزر معرف(سازنده) شیئ کتاب همان یوزر ورودی (احراز هویت شده authenticated user) به سایت میباشد مقدار True برگردون
	
class BookDeleteView(LoginRequiredMixin ,generic.DeleteView):
	model = Book
	template_name = 'books/book_delete.html'
	success_url = reverse_lazy('books:book_list')
	

