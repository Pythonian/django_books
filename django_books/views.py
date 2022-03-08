from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages

from book.models import Genre, Book
from book.forms import RequestForm


def home(request):
    books = Book.objects.all()
    genres = Genre.objects.all()[:4]
    return render(
        request, 'home.html', {'books': books, 'genres': genres})


def genres(request):
    genres = Genre.objects.all()
    return render(request, 'genres.html', {'genres': genres})


def genre_detail(request, slug):
    genre = get_object_or_404(Genre, slug=slug)
    books = genre.books.all()
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
    return render(request, 'request.html', {'form': form})


def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    favorite = bool
    if book.favorite.filter(id=request.user.id).exists():
        favorite = True
    return render(request, 'book_detail.html',
                  {'book': book, 'favorite': favorite})


def add_to_library(request, id):
    book = get_object_or_404(Book, id=id)
    if book.favorite.filter(id=request.user.id).exists():
        book.favorite.remove(request.user)
        messages.success(request, "Book removed from library")
    else:
        book.favorite.add(request.user)
        messages.success(request, "Book added to library")
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
