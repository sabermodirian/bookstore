from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import  generic # CBV :Class Base View

from books.models import Book


# Create your views here.

class BooklistView(generic.ListView):
	model = Book
	template_name = 'books/book_list.html'
	context_object_name = 'books'
	

class BookDetailsView(generic.DetailView):
	model = Book
	template_name = 'books/book_details.html'
	
class BookCreateView(generic.CreateView):
	model = Book
	fields = ['title' , 'author' , 'description' , 'price']
	template_name =  'books/book_create.html'
	success_url = reverse_lazy('books:book_details', kwargs={'pk': self.object.pk} )
	# #
	def get_success_url(self) :
	 	return reverse_lazy('books:book_details' , kwargs = {'pk' : self.object.pk})
	


	

