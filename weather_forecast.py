import requests
import os

key = os.environ.get('WEATHER_KEY')

weather_forecast_url = f'http://api.openweathermap.org/data/2.5/forecast'

def main():
    """"""

def get_location():
    """Get location input from user to determine where
    forecast should be retrieved from"""
    city, country = '', ''

    while len(city) == 0:
        city = input('Enter the name of the city').strip()
    
    while len(country) != 2 or not country.isalpha():
        country = input('Enter the 2-letter country code: ').strip()

    location = f'{city}, {country}'
    return location
        

def get_weather_forecast(location, key):
    """Retrieve API response data and catch errors."""
    try:
        query = {'q': location, 'units': 'imperial', 'appid': key}
        response = requests.get(weather_forecast_url, params=query)
        response.raise_for_status()
        data = response.json()
        return data, None
    except Exception as e:
        print(e) # TODO switch to log instead of print
        return None, e

if __name__ == '__main__':
    main()