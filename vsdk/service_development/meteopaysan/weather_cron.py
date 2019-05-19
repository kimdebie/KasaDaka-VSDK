from vsdk.service_development.models.cercle import Cercle
from vsdk.service_development.models.weather import Weather

from django.conf import settings

import json
import urllib.request

# Returns the weather data for a specific cercle
def GetWeatherData(cercle):
    webURL = urllib.request.urlopen(settings.API + str(cercle) + settings.API_KEY)
    encoding = webURL.info().get_content_charset('utf-8')
    serialized_data = webURL.read()
    weather_data = json.loads(serialized_data.decode(encoding))
    return weather_data


def ProcessWeatherData():
    cercles = Cercle.objects.all()
    metrics = settings.WEATHER_API_KEEP

    # For each cercle get the data 
    # Keep only the fields that we are interested in 
    # and build the model
    for cercle in cercles:
        weather_data = GetWeatherData(cercle.weather_api_id)
        for items in weather_data['data']:
            model = Weather()
            for item in items:
                if item in metrics:
                    if item == 'weather':
                        model.code = items[item]['code']
                        model.description = items[item]['description']
                    else:
                        setattr(model, item, items[item])
            model.cercle = cercle.name
            
            # Process the object
            # Update its values if it exists or add a new one
            try:
                existing_weather  = Weather.objects.get(cercle = model.cercle, valid_date = model.valid_date)
                for field in model._meta.get_fields():
                    # We don't want to update the id
                    if field.name != 'id':  
                        setattr(existing_weather, field.name, getattr(model, field.name))
                        existing_weather.save()
            except Weather.DoesNotExist:
                model.save()
            