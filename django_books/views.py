from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages

from story.models import Story
from book.models import Genre, Book
from book.forms import RequestForm


def home(request):
    books = Book.objects.all()[:4]
    genres = Genre.objects.order_by('?')[:4]
    stories = Story.objects.all()[:4]
    return render(
        request, 'home.html',
        {'books': books, 'genres': genres, 'stories': stories})


def genres(request):
    genres = Genre.objects.all()
    return render(request, 'genres.html', {'genres': genres})


def books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})


def stories(request):
    stories = Story.objects.all()
    return render(request, 'stories.html', {'stories': stories})


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
        if request.user.is_authenticated:
            full_name = request.user.first_name + ' ' + request.user.last_name
            initial_data = {
                'full_name': full_name,
                'email': request.user.email,
            }
            form = RequestForm(initial=initial_data)
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
