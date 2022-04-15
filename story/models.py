from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.urls import reverse

from book.models import Genre


class Story(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    category = models.ForeignKey(
        Genre, blank=True, null=True,
        on_delete=models.SET_NULL)
    description = models.TextField(max_length=2000)
    impressions = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='stories',
        on_delete=models.CASCADE)
    poster = models.ImageField(upload_to='posters')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('story:detail',
                       kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Chapter(models.Model):
    story = models.ForeignKey(
        Story, on_delete=models.CASCADE, related_name='chapters')
    order = models.PositiveSmallIntegerField(
        'Chapter number', unique=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    impressions = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
