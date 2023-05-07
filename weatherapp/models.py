from django.db import models

class Outfits(models.Model):
    cold_weather_clothing = models.ImageField(upload_to='cold_outfits')
    hot_weather_clothing = models.ImageField(upload_to='hot_outfits')


    def __str__(self):
        return str(self.id)