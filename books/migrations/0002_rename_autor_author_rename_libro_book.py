# Generated by Django 5.0.7 on 2024-08-02 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='autor',
            new_name='author',
        ),
        migrations.RenameModel(
            old_name='libro',
            new_name='book',
        ),
    ]
