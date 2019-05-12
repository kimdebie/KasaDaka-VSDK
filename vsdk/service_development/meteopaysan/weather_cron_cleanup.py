from vsdk.service_development.models.weather import Weather

from datetime import date

# Removes all the entries that correspond to past dates
def CleanupWeatherData():
    try:
        print("Starting weather cleanup...")    
        old_weather_entries = Weather.objects.filter(valid_date__lt = date.today())
        for entry in old_weather_entries:
            print("Removed entry valid_date: ", entry.valid_date)
            entry.delete()
    except Weather.DoesNotExist:
        print("Past weather entry does not exist")
    print("Finished weather cleanup...")