from django.contrib import admin
from .models import Book , Comment
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	model = Book
	
@admin.register(Comment)
class ModelNameAdmin(admin.ModelAdmin):
	model = Comment
	list_display = ('user' , 'book','text','recommend', 'is_active' ,'created_at',)
	list_filter = ['created_at' , 'book']
	search_fields = ['text' , 'user__username']
	ordering = ['-created_at']
	
