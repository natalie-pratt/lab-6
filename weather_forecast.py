import requests
import os

key = os.environ.get('WEATHER_KEY')

weather_forecast_url = f'http://api.openweathermap.org/data/2.5/forecast'
query = {'q': 'minneapolis', 'units': 'imperial', 'appid': key}

def main():
    """"""


def get_weather_forecast(url, query):
    """Retrieve API response data and catch errors."""
    response = requests.get(weather_forecast_url)
    
if __name__ == '__main__':
    main()