import requests
import os
from datetime import datetime
import logging

key = os.environ.get('WEATHER_KEY')
weather_forecast_url = f'http://api.openweathermap.org/data/2.5/forecast'

# Set up logger
logger = logging.getLogger()
logger.setLevel(logging.ERROR) # Set level to error - for instance, 404 when requesting from API
log_formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s') # Format log entries

log_file_handler = logging.FileHandler('logs.log') # File handler to write to log file
log_file_handler.setLevel(logging.ERROR) # Set level to ERROR
log_file_handler.setFormatter(log_formatter) # Format log using formatter created previously

logger.addHandler(log_file_handler) # Add the handler 


def main():
    """Calls functions and holds main code to be run
    at beginning of program"""

    location = get_location() # Get location from function
    weather_data, error = get_weather_data(location, key) # Tuple will either consist of data, and None; or None, and error. Depending on whether there is an error.

    if error:
        display_message('Sorry, could not retrieve weather data.') 
    else:
        get_weather_forecast(weather_data)


def get_location():
    """Get location input from user to determine where
    forecast should be retrieved from"""

    city, country = '', ''

    while len(city) == 0: # Loop through until user enters a valid city (in this case, valid just means not null)
        city = input('Enter the name of the city: ').strip() # .strip() to remove leading and trailing spaces from string
    
    while len(country) != 2 or not country.isalpha(): # Loop through until user enters a valid country code. Must be 2 characters and alphabetical 
        country = input('Enter the 2-letter country code: ').strip()

    location = f'{city}, {country}' # Set location values as user answers and return
    return location
        

def get_weather_data(location, key):
    """Retrieve API response data and catch errors."""
    
    try:
        query = {'q': location, 'units': 'imperial', 'appid': key} # Query paramaters (location of forecast, temp units, and API key) to be added to URL/API call
        response = requests.get(weather_forecast_url, params=query) # Request response and add query paramaters
        response.raise_for_status() # If error codes between 400-599 (client/server) are thrown, this will raise an exception
        data = response.json() 
        return data, None # Returns data if successful, and returns None because there was no error

    except Exception as e:
        logging.error(e)
        return None, e # Returns None because the data was not successfully retrieved, and returns error


def get_weather_forecast(data):
    """Get list of forecasts from response data
        to be looped over and displayed to user"""

    list_of_forecasts = data['list']

    display_message('*** Forecast in 3 hour increments for the next 5 days ***')

    for forecast in list_of_forecasts:
        date_format = '%d-%m-%Y %H:%M' # Using UTC time - decided this because weather forecast can be found for anywhere in the world
                                        # and having local time wouldn't make very much sense for somewhere in the world not using the same time
        timestamp = forecast['dt']
        forecast_date = datetime.utcfromtimestamp(timestamp) # Convert timestamp into UTC datetime
        formatted_forecast_date = forecast_date.strftime(date_format) # Format date into previously stated format

        temp = forecast['main']['temp']
        wind_speed = forecast['wind']['speed']

        display_formatted_weather_forecast(formatted_forecast_date, temp, wind_speed)


def display_formatted_weather_forecast(date, temp, wind_speed):
    print(f'\nDate & Time (UTC): {date}\nTemperature: {temp}\nWind speed: {wind_speed}')


def display_message(msg):
    print(f'\n{msg}\n')


if __name__ == '__main__':
    main()