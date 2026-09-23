
from django.shortcuts import render , get_object_or_404
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

def book_details_view(request, pk):
    book = get_object_or_404(Book, pk=pk) # get book object
    
    book_comments= book.cmnts_rel.all() # get book's comments برای گرفتن کامنتهای هر کتاب با استفاده از related_name
    if request.method != 'POST' :
	    comment_form = CommentForm(request.POST)
	    if comment_form.is_valid():
		    new_cmnt = comment_form.save(commit = False)
		    new_cmnt.book = book
		    new_cmnt.user = request.user
		    new_cmnt.save()
		    comment_form = comment_form()
	# else:
	# 	comment_form = comment_form()
	
    
    return render(request,
                  'books/book_details.html',
                  {'book': book,
                   'comments' : book_comments ,
                   'comment_form' : comment_form,
                   })

	
	
class BookCreateView(generic.CreateView):
	model = Book
	fields = ['title' , 'author' , 'description' , 'price', 'bk_cover']
	template_name =  'books/book_create.html' #'books/book_create_and_update.html'
	# success_url = reverse_lazy('books:book_details', kwargs={'pk': self.object.pk} )
	# #
	def get_success_url(self) :
	 	return reverse_lazy('books:book_details' , kwargs = {'pk' : self.object.pk})
	
class BookUpdateView(generic.UpdateView):
	model = Book
	fields = ['title' , 'author' , 'description' , 'bk_cover']
	template_name =  'books/book_update.html' #'books/book_create_and_update.html'
	
class BookDeleteView(generic.DeleteView):
	model = Book
	template_name = 'books/book_delete.html'
	success_url = reverse_lazy('books:book_list')
	

