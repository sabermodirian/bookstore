from django.shortcuts import render
from django.views import  generic # CBV :Class Base View

from books.models import Book


# Create your views here.

class BooklistView(generic.ListView):
	model = Book
	template_name = 'books/book_list.html'
	context_object_name = 'books'
