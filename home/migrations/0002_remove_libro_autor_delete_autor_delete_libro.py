# Generated by Django 5.0.7 on 2024-08-02 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='autor',
        ),
        migrations.DeleteModel(
            name='autor',
        ),
        migrations.DeleteModel(
            name='libro',
        ),
    ]
