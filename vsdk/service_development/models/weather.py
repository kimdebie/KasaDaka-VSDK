from django.db import models

class Weather(models.Model):
    temperature = models.FloatField()   
    rainfall = models.IntegerField()    # % Chance
    clouds = models.IntegerField()      # % Coverage
    wind = models.FloatField()