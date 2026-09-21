
from django.urls import path

from books.views import BookDeleteView , book_details_view, BookUpdateView , BooklistView , BookCreateView

app_name = 'books'

urlpatterns = [
	path('', BooklistView.as_view() , name = 'book_list'),
	path('<int:pk>/' , book_details_view  , name = 'book_details' ),
	path('create/' , BookCreateView.as_view() , name = 'book_create'),
	path('<int:pk>/edit/' , BookUpdateView.as_view() , name = 'book_update'),
	path('<int:pk>/delete/' , BookDeleteView.as_view() , name = 'book_delete'),
]