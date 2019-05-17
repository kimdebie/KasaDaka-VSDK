from vsdk.service_development.models.vs_element import VoiceServiceSubElement

from vsdk.service_development.models.cercle import Cercle
from vsdk.service_development.models.weather import Weather
from vsdk.service_development.models.crop import Crop

from datetime import date

def PlantDecision(language_code, cercle_name, crop_name):
    crop_conditions = Crop.objects.get(name = crop_name.lower())
    avg_weather = GetAverageWeather(cercle_name)

    error_rate = 0.05
    conditions_violated = False

    # Snow
    if crop_conditions.snow is not None and conditions_violated is False:
        if avg_weather.snow != crop_conditions.snow:
            print("[PlantDecision] Violated snow - AVG: ", avg_weather.snow, " CROP: ", crop_conditions.snow)
            conditions_violated = True

    if crop_conditions.snow_depth is not None and conditions_violated is False:
        if avg_weather.snow_depth != crop_conditions.snow_depth:
            print("[PlantDecision] Violated snow_depth - AVG: ", avg_weather.snow_depth, " CROP: ", crop_conditions.snow_depth)
            conditions_violated = True


    # Rh
    if crop_conditions.rh is not None and conditions_violated is False:
        plus_5 = (crop_conditions.rh * error_rate) + crop_conditions.rh
        minus_5 = crop_conditions.rh - (crop_conditions.rh * error_rate)

        if (avg_weather.rh >= plus_5 or avg_weather.rh <= minus_5):
            print("[PlantDecision] Violated rh - AVG: ", avg_weather.rh, " CROP: ", crop_conditions.rh, " 5% +/-: ", plus_5, ",", minus_5)
            conditions_violated = True


    # Precip
    if crop_conditions.precip is not None and conditions_violated is False:
        plus_5 = (crop_conditions.precip * error_rate) + crop_conditions.precip
        minus_5 = crop_conditions.precip - (crop_conditions.precip * error_rate)

        if (avg_weather.precip >= plus_5 or avg_weather.precip <= minus_5):
            print("[PlantDecision] Violated precip - AVG: ", avg_weather.precip, " CROP: ", crop_conditions.precip, " 5% +/-: ", plus_5, ",", minus_5)
            conditions_violated = True


    # Temperature
    if crop_conditions.temp is not None and conditions_violated is False:
        plus_5 = (crop_conditions.temp * error_rate) + crop_conditions.temp
        minus_5 = crop_conditions.temp - (crop_conditions.temp * error_rate)

        if (avg_weather.temp >= plus_5 or avg_weather.temp <= minus_5):
            print("[PlantDecision] Violated temp - AVG: ", avg_weather.temp, " CROP: ", crop_conditions.temp, " 5% +/-: ", plus_5, ",", minus_5)
            conditions_violated = True

    if crop_conditions.max_temp is not None and conditions_violated is False:
        plus_5 = (crop_conditions.max_temp * error_rate) + crop_conditions.max_temp
        minus_5 = crop_conditions.max_temp - (crop_conditions.max_temp * error_rate)

        if (avg_weather.max_temp >= plus_5 or avg_weather.max_temp <= minus_5):
            print("[PlantDecision] Violated max_temp - AVG: ", avg_weather.max_temp, " CROP: ", crop_conditions.max_temp, " 5% +/-: ", plus_5, ",", minus_5)
            conditions_violated = True 
    
    if crop_conditions.min_temp is not None and conditions_violated is False:
        plus_5 = (crop_conditions.min_temp * error_rate) + crop_conditions.min_temp
        minus_5 = crop_conditions.min_temp - (crop_conditions.min_temp * error_rate)

        if (avg_weather.min_temp >= plus_5 or avg_weather.min_temp <= minus_5):
            print("[PlantDecision] Violated min_temp - AVG: ", avg_weather.min_temp, " CROP: ", crop_conditions.min_temp, " 5% +/-: ", plus_5, ",", minus_5)
            conditions_violated = True 
    
    
    # Clouds
    if crop_conditions.clouds is not None and conditions_violated is False:
        plus_5 = (crop_conditions.clouds * error_rate) + crop_conditions.clouds
        minus_5 = crop_conditions.clouds - (crop_conditions.clouds * error_rate)

        if (avg_weather.clouds >= plus_5 or avg_weather.clouds <= minus_5):
            print("[PlantDecision] Violated clouds - AVG: ", avg_weather.clouds, " CROP: ", crop_conditions.clouds, " 5% +/-: ", plus_5, ",", minus_5)
            conditions_violated = True 

    if crop_conditions.clouds_low is not None and conditions_violated is False:
        plus_5 = (crop_conditions.clouds_low * error_rate) + crop_conditions.clouds_low
        minus_5 = crop_conditions.clouds_low - (crop_conditions.clouds_low * error_rate)

        if (avg_weather.clouds_low >= plus_5 or avg_weather.clouds_low <= minus_5):
            print("[PlantDecision] Violated clouds_low - AVG: ", avg_weather.clouds_low, " CROP: ", crop_conditions.clouds_low, " 5% +/-: ", plus_5, ",", minus_5)
            conditions_violated = True 

    if crop_conditions.clouds_mid is not None and conditions_violated is False:
        plus_5 = (crop_conditions.clouds_mid * error_rate) + crop_conditions.clouds_mid
        minus_5 = crop_conditions.clouds_mid - (crop_conditions.clouds_mid * error_rate)

        if (avg_weather.clouds_mid >= plus_5 or avg_weather.clouds_mid <= minus_5):
            print("[PlantDecision] Violated clouds_mid - AVG: ", avg_weather.clouds_mid, " CROP: ", crop_conditions.clouds_mid, " 5% +/-: ", plus_5, ",", minus_5)
            conditions_violated = True 

    if crop_conditions.clouds_hi is not None and conditions_violated is False:
        plus_5 = (crop_conditions.clouds_hi * error_rate) + crop_conditions.clouds_hi
        minus_5 = crop_conditions.clouds_hi - (crop_conditions.clouds_hi * error_rate)

        if (avg_weather.clouds_hi >= plus_5 or avg_weather.clouds_hi <= minus_5):
            print("[PlantDecision] Violated clouds_hi - AVG: ", avg_weather.clouds_hi, " CROP: ", crop_conditions.clouds_hi, " 5% +/-: ", plus_5, ",", minus_5)
            conditions_violated = True 


    if conditions_violated is True:
        wav_name = crop_name + "-prediction-no"
    else:
        wav_name = crop_name + "-prediction-yes"
    wav = VoiceServiceSubElement.objects.get(name = wav_name)
    return wav.id


def GetAverageWeather(cercle_name):
    weather_forecast = Weather.objects.filter(valid_date__gte = date.today(), cercle = cercle_name.lower())

    # We are caclulating only the metrics that are taken into consideration in the Crops model
    snow = sum(weather.snow for weather in weather_forecast)/len(weather_forecast)
    snow_depth = sum(weather.snow_depth for weather in weather_forecast)/len(weather_forecast)
    rh = sum(weather.rh for weather in weather_forecast)/len(weather_forecast)
    precip = sum(weather.precip for weather in weather_forecast)/len(weather_forecast)
    temp = sum(weather.temp for weather in weather_forecast)/len(weather_forecast)
    max_temp = sum(weather.max_temp for weather in weather_forecast)/len(weather_forecast)
    min_temp = sum(weather.min_temp for weather in weather_forecast)/len(weather_forecast)
    clouds = sum(weather.clouds for weather in weather_forecast)/len(weather_forecast)
    clouds_low = sum(weather.clouds_low for weather in weather_forecast)/len(weather_forecast)
    clouds_mid = sum(weather.clouds_mid for weather in weather_forecast)/len(weather_forecast)
    clouds_hi = sum(weather.clouds_hi for weather in weather_forecast)/len(weather_forecast)
    
    avg_weather = Weather()
    avg_weather.snow = snow
    avg_weather.snow_depth = snow_depth
    avg_weather.rh = rh
    avg_weather.precip = precip
    avg_weather.temp = temp
    avg_weather.max_temp = max_temp
    avg_weather.min_temp = min_temp
    avg_weather.clouds = clouds
    avg_weather.clouds_low = clouds_low
    avg_weather.clouds_mid = clouds_mid
    avg_weather.clouds_hi = clouds_hi

    return avg_weather
