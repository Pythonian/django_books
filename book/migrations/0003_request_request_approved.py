# Generated by Django 4.0.4 on 2022-12-20 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_slug_alter_book_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='request_approved',
            field=models.BooleanField(default=False),
        ),
    ]
