# Generated by Django 4.0 on 2021-12-15 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_flight_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('city', models.CharField(max_length=64)),
            ],
        ),
    ]
