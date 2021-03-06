# Generated by Django 3.2.9 on 2022-02-20 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batterystorage',
            fields=[
                ('id', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('operationstrategy', models.CharField(max_length=300, null=True)),
                ('feedinLimitations', models.IntegerField(null=True)),
                ('usablecapacity', models.CharField(max_length=300, null=True)),
                ('ratedpower', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Batterystorage',
            },
        ),
        migrations.CreateModel(
            name='Chp',
            fields=[
                ('id', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('technologychp', models.CharField(max_length=300, null=True)),
                ('electricalpower', models.IntegerField(null=True)),
                ('thermalpower', models.IntegerField(null=True)),
                ('operationstrategy', models.BooleanField(max_length=20, null=True)),
            ],
            options={
                'verbose_name_plural': 'CHP',
            },
        ),
        migrations.CreateModel(
            name='Electricvehicles',
            fields=[
                ('id', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('loadpointcount', models.BooleanField(null=True)),
                ('totalpowerofload', models.BooleanField(null=True)),
                ('profiletype', models.CharField(max_length=300, null=True)),
                ('prohabilityofpluggin', models.BooleanField(null=True)),
                ('kmperyear', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gasheater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('termalpowerneeded', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Gasheater',
            },
        ),
        migrations.CreateModel(
            name='Heatpump',
            fields=[

                ('technology', models.CharField(max_length=300, null=True)),
                ('model', models.CharField(max_length=300, null=True)),
            ],
            options={
                'verbose_name_plural': 'Heatpump',
            },
        ),
        migrations.CreateModel(
            name='Hydrogenstorage',
            fields=[
                ('id', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('usablecapacity', models.BooleanField(null=True)),
                ('ratedpowerelectrolyser', models.IntegerField(null=True)),
                ('ratedpowerfuelcell', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Hydrogenstorage',
            },
        ),
        migrations.CreateModel(
            name='Mfh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numofdwellings', models.PositiveIntegerField(null=True)),
                ('electricalenergyconsumption', models.BooleanField(null=True)),
                ('dhwenergyconsumption', models.BooleanField(null=True)),
                ('thermalbuildingstandard', models.CharField(max_length=20, null=True)),
                ('buildingsize', models.PositiveIntegerField(null=True)),
            ],
            options={
                'verbose_name_plural': 'MFH',
            },
        ),
        migrations.CreateModel(
            name='Photovoltaic',
            fields=[
                ('id', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('genpower', models.BooleanField(null=True)),
                ('azimut', models.IntegerField(null=True)),
                ('elevation', models.IntegerField(null=True)),
                ('inverterpower', models.BooleanField(max_length=20, null=True)),
            ],
            options={
                'verbose_name_plural': 'Photovoltaic',
            },
        ),
        migrations.CreateModel(
            name='Sfh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numofpersons', models.PositiveIntegerField(null=True)),
                ('electricalenergyconsumption', models.BooleanField()),
                ('thermalbuildingstandard', models.CharField(max_length=20, null=True)),
                ('buildingsize', models.PositiveIntegerField(null=True)),
            ],
            options={
                'verbose_name_plural': 'SFH',
            },
        ),
    ]
