from django.contrib import admin
from .models import (Book, BookInstance, Genre, Author)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('id', 'imprint', 'book')
        }),
       ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
    list_display = ['status', 'due_back', 'id']


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

class AuthorInstanceInline(admin.TabularInline):
    model = Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birthday', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birthday', 'date_of_death')]
    inlines = [AuthorInstanceInline]