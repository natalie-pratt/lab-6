import requests
import os

key = os.environ.get('WEATHER_KEY')

weather_forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q=minneapolis,us&units=imperial&appid={key}'