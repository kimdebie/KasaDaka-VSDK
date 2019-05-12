from vsdk.service_development.models.weather import Weather
from vsdk.service_development.models.crop import Crop

from datetime import date

user_cercle = "Sikasso".lower()
user_crop = "Rice".lower()
current_date = date.today()

def PlantDecision():
    weather_forecast = Weather.objects.filter(valid_date__gte = date.today(), cercle = user_cercle)
    crop_conditions = Crop.objects.get(name = user_crop)

    # Apply logic here