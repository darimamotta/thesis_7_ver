# Generated by Django 3.2.7 on 2022-03-22 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0009_auto_20220322_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='economic',
            name='tos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='technology.tos'),
        ),
    ]
