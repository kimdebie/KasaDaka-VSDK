import json
import urllib.request

# Return weather data for a specific cercle
def GetWeatherData(cercle):
    API = 'http://api.weatherbit.io/v2.0/forecast/daily?&city_id='    
    API_KEY = "&key=57bca00927914f9f95a78579d637133e"

    webURL = urllib.request.urlopen(API + cercle + API_KEY)
    encoding = webURL.info().get_content_charset('utf-8')
    serialized_data = webURL.read()
    weather_data = json.loads(serialized_data.decode(encoding))
    return weather_data


def ProcessData():
    # Load cercles
    with open('cercles.json') as f:
        data = json.load(f)
    
    # Metrics to keep
    metrics = [line.rstrip('\n') for line in open('weather_metrics_keep')]

    # For each cercle
    for cercle in data['cercles']:
        model = {}
        weather_data = GetWeatherData(str(cercle['id']))
        for items in weather_data['data']:
            for item in items:
                if item in metrics:
                    if item == 'weather':
                        model['code'] = items[item]['code']
                        model['description'] = items[item]['description']
                    else:
                        model[item] = items[item]
            model['cercle'] = cercle['name']

            ### PROCESS ENTRY ###
            # Get weather entry (by valid_date and cercle):
                # If it exists
                    # Update existing entry
                # else
                    # Insert
            print(json.dumps(model, indent=4, sort_keys=True))

if __name__ == "__main__":
    ProcessData()