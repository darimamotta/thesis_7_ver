# Generated by Django 3.2.9 on 2022-03-08 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesis', '0011_buildingprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='tos',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]