
from django.urls import path

from books.views import BooklistView

urlpatterns = [
	path('', BooklistView.as_view() , name = 'book_list'),
	
]