from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=60, primary_key = True)
    clouds = models.FloatField(null = True)
    clouds_hi = models.FloatField(null = True)
    clouds_mid = models.FloatField(null = True)
    clouds_low = models.FloatField(null = True)
    min_temp = models.FloatField(null = True)   
    max_temp = models.FloatField(null = True)
    temp = models.FloatField(null = True)
    precip = models.FloatField(null = True)
    rh = models.FloatField(null = True)
    snow = models.FloatField(null = True)
    snow_depth = models.FloatField(null = True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Crop, self).save(*args, **kwargs)

        