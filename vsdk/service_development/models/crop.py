from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=60, primary_key = True)
    clouds = models.FloatField(default = -1, blank = True)
    clouds_hi = models.FloatField(default = -1, blank = True)
    clouds_mid = models.FloatField(default = -1, blank = True)
    clouds_low = models.FloatField(default = -1, blank = True)
    min_temp = models.FloatField(default = -1, blank = True)   
    max_temp = models.FloatField(default = -1, blank = True)
    temp = models.FloatField(default = -1, blank = True)
    precip = models.FloatField(default = -1, blank = True)
    rh = models.FloatField(default = -1, blank = True)
    snow = models.FloatField(default = -1, blank = True)
    snow_depth = models.FloatField(default = -1, blank = True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Crop, self).save(*args, **kwargs)

        