# Generated by Django 4.0.3 on 2022-03-22 19:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('registration_date', models.DateField()),
                ('success_flights', models.IntegerField()),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('year_of_manufacture', models.DateField()),
                ('available_places', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_point', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('transfer_points_amount', models.IntegerField(blank=True, default=0)),
                ('start_time', models.DateTimeField()),
                ('arriving_time', models.IntegerField()),
                ('price', models.FloatField()),
                ('available_tickets', models.IntegerField(null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flights', to='airwaysinfoapp.company')),
                ('plane', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='flights', to='airwaysinfoapp.plane')),
            ],
        ),
    ]
