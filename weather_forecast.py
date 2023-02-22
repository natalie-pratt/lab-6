import requests
import os

key = os.environ.get('WEATHER_KEY')

weather_forecast_url = f'http://api.openweathermap.org/data/2.5/forecast'
query = {'q': 'minneapolis', 'units': 'imperial', 'appid': key}

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
        

def get_weather_forecast():
    """Retrieve API response data and catch errors."""
    response = requests.get(weather_forecast_url)
    

if __name__ == '__main__':
    main()