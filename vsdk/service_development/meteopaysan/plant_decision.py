from vsdk.service_development.models.cercle import Cercle
from vsdk.service_development.models.weather import Weather
from vsdk.service_development.models.crop import Crop

from datetime import date

def PlantDecision(language_code, cercle_name, crop_name):
    weather_forecast = Weather.objects.filter(valid_date__gte = date.today(), cercle = cercle_name.lower())
    crop_conditions = Crop.objects.get(name = crop_name.lower())
    # Apply logic here
    # clouds_hi = models.FloatField(null = True, blank = True)
    # clouds_mid = models.FloatField(null = True, blank = True)
    # clouds_low = models.FloatField(null = True, blank = True)
    # description = models.CharField(max_length=60, null = True, blank = True)
    # min_temp = models.FloatField(null = True, blank = True)   
    # max_temp = models.FloatField(null = True, blank = True)
    # precip = models.FloatField(null = True, blank = True)
    # rh = models.FloatField(null = True, blank = True)
    # snow = models.FloatField(null = True, blank = True)
    # snow_depth = models.FloatField(null = True, blank = True)

    #Templates added name
    # Post get by name -> If name does not include crop or cercle we are fcked
    # Return the ID from VoiceServiceElement -> VoiceServiceSubElement (ID of the prediction by name) 
    