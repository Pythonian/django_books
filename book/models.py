from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Genre(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100,
                             help_text="The title of the book.")
    slug = models.SlugField(max_length=100)
    genre = models.ForeignKey(
        Genre, on_delete=models.PROTECT, related_name='books')
    book_file = models.FileField(upload_to='books')
    author = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='covers')
    publisher = models.CharField(max_length=100)
    publication_date = models.DateField(
        verbose_name="Date the book was published.")
    pages = models.PositiveIntegerField()
    summary = models.TextField()
    isbn = models.CharField(max_length=20,
                            verbose_name="ISBN number of the book.")
    favorite = models.ManyToManyField(
        User, related_name='favorites', blank=True)
    impressions = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Request(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} requested for {self.title}"
