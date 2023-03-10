# Generated by Django 4.1.3 on 2022-11-23 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='nasa_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voltage_measured', models.FloatField()),
                ('current_measured', models.FloatField()),
                ('temperature_measured', models.FloatField()),
                ('current_load', models.FloatField()),
                ('voltage_load', models.FloatField()),
                ('time', models.FloatField()),
                ('capacity', models.FloatField()),
                ('cycle', models.IntegerField()),
            ],
        ),
    ]
