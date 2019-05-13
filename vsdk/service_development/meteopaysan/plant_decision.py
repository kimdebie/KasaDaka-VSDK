from vsdk.service_development.models.cercle import Cercle
from vsdk.service_development.models.weather import Weather
from vsdk.service_development.models.crop import Crop

from datetime import date

def PlantDecision(language_id, cercle_id, crop_id):
    user_cercle = Cercle.objects.get(id = cercle_id)
    weather_forecast = Weather.objects.filter(valid_date__gte = date.today(), cercle = user_cercle.name)

    user_crop = Crop.objects.get(id = crop_id)
    crop_conditions = Crop.objects.get(name = user_crop.name)


    # Apply logic here
    

    # Return the wav file
