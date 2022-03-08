from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import login

from book.models import Book

from .forms import SignUpForm


class SignUpView(SuccessMessageMixin, CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_message = "Your account was created successfully"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def profile(request):
    books = Book.objects.filter(favorite=request.user)
    favorite = bool
    if Book.objects.filter(id=request.user.id).exists():
        favorite = True
    return render(
        request, 'profile.html',
        {'books': books, 'favorite': favorite})


# def compare_vehicles(request):
#     vehicles = Vehicle.objects.filter(
#         is_available=True).filter(compares=request.user)[:3]
#     return render(
#         request, 'vehicle/compare.html', {'vehicles': vehicles})
