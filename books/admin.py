from django.contrib import admin
from .models import Book , Comment
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	model = Book
	
@@admin.register(Comment)
class ModelNameAdmin(admin.ModelAdmin):
	model = Comment
 
	
