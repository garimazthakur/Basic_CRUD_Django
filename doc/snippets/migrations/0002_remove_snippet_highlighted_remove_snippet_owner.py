# Generated by Django 4.0.4 on 2022-04-27 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='highlighted',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='owner',
        ),
    ]