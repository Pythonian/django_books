# Generated by Django 4.0.4 on 2022-08-19 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(blank=True, max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The title of the book.', max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('book_file', models.FileField(upload_to='books')),
                ('author', models.CharField(max_length=100)),
                ('cover', models.ImageField(upload_to='covers')),
                ('publisher', models.CharField(max_length=100)),
                ('publication_date', models.DateField(verbose_name='Date the book was published.')),
                ('pages', models.PositiveIntegerField()),
                ('summary', models.TextField()),
                ('isbn', models.CharField(max_length=20, verbose_name='ISBN number.')),
                ('impressions', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('favorite', models.ManyToManyField(blank=True, related_name='favorites', to=settings.AUTH_USER_MODEL)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='book.genre')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
