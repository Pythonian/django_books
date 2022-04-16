from django.db import models
from django.conf import settings
from django.urls import reverse

User = settings.AUTH_USER_MODEL


class Genre(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre_detail',
                       kwargs={'slug': self.slug})


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
                            verbose_name="ISBN number.")
    favorite = models.ManyToManyField(
        User, related_name='favorites', blank=True)
    impressions = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail',
                       kwargs={'slug': self.slug})


class Request(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Book request: {self.title}"
