# Generated by Django 4.2.1 on 2023-05-05 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outfits',
            name='cold_weather_clothing',
            field=models.ImageField(upload_to='cold_outfits'),
        ),
        migrations.AlterField(
            model_name='outfits',
            name='hot_weather_clothing',
            field=models.ImageField(upload_to='hot_outfits'),
        ),
    ]