import requests

def print_first_five_paris_temperatures():
    # Your implementation goes here
    url = 'https://api.open-meteo.com/v1/forecast'
    params = {
        'latitude': 48.85,
        'longitude': 2.35,
        'hourly': 'temperature_2m'        
    }

    response = requests.get(url,params=params)
    data = response.json()
    for i in range(5):
        print(data['hourly']['temperature_2m'][i])
    pass

print_first_five_paris_temperatures()
