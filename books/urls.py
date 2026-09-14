
from django.urls import path

from books.views import BookDetailsView , BooklistView , BookCreateView

app_name = 'books'

urlpatterns = [
	path('', BooklistView.as_view() , name = 'book_list'),
	path('<int:pk>/' , BookDetailsView.as_view()  , name = 'book_details' ),
	path('create/' , BookCreateView.as_view() , name = 'book_create')
]