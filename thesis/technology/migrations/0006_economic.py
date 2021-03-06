# Generated by Django 3.2.7 on 2022-03-21 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0005_buildingprofile_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Economic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('electricity_fixed_costs_per_year', models.IntegerField(null=True)),
                ('electricity_costs_per_kWh', models.IntegerField(max_length=20, null=True)),
                ('electricity_feed_in_tariff_chp', models.IntegerField(null=True)),
                ('electricity_feed_in_tariff_for_photovoltaic', models.IntegerField(null=True)),
            ],
        ),
    ]
