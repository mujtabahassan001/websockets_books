# Generated by Django 5.1.5 on 2025-01-15 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0002_rename_user_book_published_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='published_by',
            new_name='user',
        ),
    ]
