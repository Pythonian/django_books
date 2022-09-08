import os

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from book.forms import RequestForm
from book.models import Book, Genre
from story.models import Story

from .utils import mk_paginator


def home(request):
    books = Book.objects.all()[:4]
    genres = Genre.objects.order_by('?')[:4]
    stories = Story.objects.all()[:4]
    return render(
        request, 'home.html',
        {'books': books, 'genres': genres, 'stories': stories})


def genres(request):
    genres = Genre.objects.all()
    genres = mk_paginator(request, genres, 12)
    return render(request, 'genres.html', {'genres': genres})


def books(request):
    books = Book.objects.all()
    books = mk_paginator(request, books, 8)
    return render(request, 'books.html', {'books': books})


def stories(request):
    stories = Story.objects.all()
    stories = mk_paginator(request, stories, 8)
    return render(request, 'stories.html', {'stories': stories})


def genre_detail(request, slug):
    genre = get_object_or_404(Genre, slug=slug)
    books = genre.books.all()
    books = mk_paginator(request, books, 8)
    return render(request, 'genre_detail.html',
                  {'genre': genre, 'books': books})


def request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your book request was successfully sent.")
            return redirect('request')
    else:
        form = RequestForm()
        if request.user.is_authenticated:
            full_name = request.user.first_name + ' ' + request.user.last_name
            initial_data = {
                'full_name': full_name,
                'email': request.user.email,
            }
            form = RequestForm(initial=initial_data)
    return render(request, 'request.html', {'form': form})


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    favorite = bool
    if book.favorite.filter(id=request.user.id).exists():
        favorite = True
    return render(request, 'book_detail.html',
                  {'book': book, 'favorite': favorite})


@login_required
def book_read_online(request, id):
    book = get_object_or_404(Book, id=id)
    filepath = os.path.join(settings.MEDIA_ROOT, str(book.book_file))
    response = FileResponse(open(filepath, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = 'inline'
    return response

    # try:
    #     response = FileResponse(open(filepath, 'rb'),
    #                             content_type='application/pdf')
    #     response['Content-Disposition'] = 'inline'
    #     return response
    # except FileNotFoundError:
    #     raise Http404()


@login_required
def add_to_library(request, id):
    book = get_object_or_404(Book, id=id)
    if book.favorite.filter(id=request.user.id).exists():
        book.favorite.remove(request.user)
        messages.success(request, "Book removed from library")
    else:
        book.favorite.add(request.user)
        messages.success(request, "Book added to library")
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
