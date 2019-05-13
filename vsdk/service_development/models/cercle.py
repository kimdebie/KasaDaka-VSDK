from django.db import models

class Cercle(models.Model):
    name = models.CharField(max_length=60, primary_key = True)
    weather_api_id = models.IntegerField(unique = True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Cercle, self).save(*args, **kwargs)

