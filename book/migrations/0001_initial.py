# Generated by Django 3.1.7 on 2022-03-08 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The title of the book.', max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('book_file', models.FileField(upload_to='books')),
                ('author', models.CharField(max_length=100)),
                ('cover', models.ImageField(upload_to='covers')),
                ('publisher', models.CharField(max_length=100)),
                ('publication_date', models.DateField(verbose_name='Date the book was published.')),
                ('pages', models.PositiveIntegerField()),
                ('isbn', models.CharField(max_length=20, verbose_name='ISBN number of the book.')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='book.genre')),
            ],
        ),
    ]