from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=60, primary_key = True)
    clouds = models.FloatField(null = True, blank = True)
    clouds_hi = models.FloatField(null = True, blank = True)
    clouds_mid = models.FloatField(null = True, blank = True)
    clouds_low = models.FloatField(null = True, blank = True)
    min_temp = models.FloatField(null = True, blank = True)   
    max_temp = models.FloatField(null = True, blank = True)
    temp = models.FloatField(null = True, blank = True)
    precip = models.FloatField(null = True, blank = True)
    rh = models.FloatField(null = True, blank = True)
    snow = models.FloatField(null = True, blank = True)
    snow_depth = models.FloatField(null = True, blank = True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Crop, self).save(*args, **kwargs)

        