from django.contrib import admin


from .models import Genre, Book, Request


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'author', 'publisher', 'pages', 'isbn']
    search_fields = ['title', 'author', 'publisher', 'isbn']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'title', 'author']
