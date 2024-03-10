# Generated by Django 5.0.2 on 2024-03-10 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline', models.CharField(max_length=100)),
                ('flight', models.CharField(max_length=12)),
                ('source_city', models.CharField(max_length=100)),
                ('departure_time', models.IntegerField(choices=[(1, 'Early_morning'), (2, 'Morning'), (3, 'Day'), (4, 'Evening'), (5, 'Night'), (6, 'Late_Night')])),
                ('stops', models.PositiveSmallIntegerField(default=0)),
                ('arrival_time', models.IntegerField(choices=[(1, 'Early_morning'), (2, 'Morning'), (3, 'Day'), (4, 'Evening'), (5, 'Night'), (6, 'Late_Night')])),
                ('destination_city', models.CharField(max_length=100)),
                ('class_type', models.IntegerField(choices=[(1, 'Econom'), (2, 'Business')])),
                ('duration', models.FloatField()),
                ('day', models.DateField()),
            ],
        ),
    ]