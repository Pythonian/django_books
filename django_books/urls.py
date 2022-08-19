"""django_books URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('story/', include('story.urls', namespace='story')),
    path('genres/', views.genres, name='genres'),
    path('books/', views.books, name='books'),
    path('stories/', views.stories, name='stories'),
    path('request/', views.request, name='request'),
    path('genre/<slug:slug>/', views.genre_detail, name='genre_detail'),
    path('book/read/<int:id>/', views.book_read_online, name='read'),
    path('book/<slug:slug>/', views.book_detail, name='book_detail'),
    path('update-library/<int:id>/',
         views.add_to_library, name='add_to_library'),
    path('', views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = 'African Lit. Admin'
admin.site.index_title = 'African Lit. Admin'
admin.site.site_title = 'Admin Dashboard'
