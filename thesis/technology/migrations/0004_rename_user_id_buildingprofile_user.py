# Generated by Django 4.0 on 2022-03-10 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0003_buildingprofile_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buildingprofile',
            old_name='user_id',
            new_name='user',
        ),
    ]
