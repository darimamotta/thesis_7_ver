# Generated by Django 4.0 on 2022-03-10 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_search_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='search',
            old_name='user_id',
            new_name='user',
        ),
    ]
