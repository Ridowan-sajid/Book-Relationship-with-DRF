from django.contrib import admin
from .models import Book, Author


@admin.register(Book)
class BookHandle(admin.ModelAdmin):
    list_display = ['id','title','author','date']

@admin.register(Author)
class AuthorHandle(admin.ModelAdmin):
    list_display = ['id','name','gender']
