from django.contrib import admin
from django.core.mail import send_mail


from .models import Genre, Book, Request


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'author', 'publisher', 'pages', 'isbn']
    search_fields = ['title', 'author', 'publisher', 'isbn']
    list_filter = ['genre']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'title', 'author', 'request_approved']
    list_filter = ['request_approved']

    def save_model(self, request, obj, form, change):
        if obj.request_approved is True:
            send_mail(
                'Congratulations! Request Completed',
                'Your book request has now been completed. Please login to the site to check it out.',
                'admin@africanlit.com',
                [obj.email],
                fail_silently=False)
        super(RequestAdmin, self).save_model(request, obj, form, change)
