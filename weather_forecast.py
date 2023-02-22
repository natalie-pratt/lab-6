import requests
import os

key = os.environ.get('WEATHER_KEY')
weather_forecast_url = f'http://api.openweathermap.org/data/2.5/forecast'

def main():
    """Calls functions and holds main code to be run
    at beginning of program"""

    location = get_location() # Get location from function
    weather_data, error = get_weather_data(location, key)

    if error:
        display_message('Sorry, could not retrieve weather data.') # TODO - add display message function to format print statements
    else:
        '' # PLACEHOLDER
        # TODO - add function call to get weather data


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
        print(e) # TODO switch to log instead of print
        return None, e # Returns None because the data was not successfully retrieved, and returns error


def display_message(msg):
    print(f'\n{msg}')


if __name__ == '__main__':
    main()