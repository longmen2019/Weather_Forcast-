'''The requests library is a powerful tool for interacting with web APIs and web services. It
simplifies the process of making HTTP requests and handling responses.'''
import logging
import requests
import os

# Configure logging
"""By setting the level to logging.INFO, this code configures the logger to record messages with a severity level of 
INFO or higher. """
logging.basicConfig(level=logging.INFO)


def get_weather_data(city_name, api_key):
    """Fetches weather data for a given city using the OpenWeatherMap API

    Args:
        city_name: The name of the city to get weather data for.
        api_key: Your OpenWeatherMap API key.

    Returns:
        A dictionary containing weather data (or None if an error occurs).
    """

    """The URL is the endpoint where you can send HTTP requests to get current weather information for 
    a specified location"""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    # Construct the full URL
    """the requests_url variable constructs the full url by combining base_url, the city name, and the API_KEY"""
    url = f"{base_url}?q={city_name}&appid={api_key}"

    """Error Handling: Added try-except blocks to handle HTTP and general errors."""
    try:
        ''' The requests.get() function sends a GET request to the constructed URL. '''
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        """Configured logging to capture error and other information"""
        logging.error(f"HTTP error occurred: {http_err}")
    except Exception as err:
        logging.error(f"An error occurred: {err}")
    return None

def main():
    """Prompts user for city name, fetches weather data, and displays it."""

    """An API key is a unique identifier used to authenticate requests associated with your account. It ensures
    that the requests you make to the OpenWeatherMap API are authorized and can be tracked."""
    """Moved the API key to an environment variable."""
    api_key = os.getenv("OPENWEATHERMAP_API_KEY", "5e756eb1b406ec434b7debcf93457aed")
    if not api_key:
        logging.error("API key not found, Please set the OPENWEATHERMAP_API_KEY environment variable")
        return

    """specifies the city for which you want to get the weather data"""
    """Input Validation: Added a check to ensure the city name is not empty."""
    city_name = input("Enter a city name: ").strip()

    weather_data = get_weather_data(city_name, api_key)

    # Check if the request was successful
    if weather_data:
        weather = weather_data["weather"][0]["description"]
        country = weather_data["sys"]["country"]
        temperature = round(weather_data["main"]["temp"] - 273.15, 2)
        feels_like = round(weather_data["main"]["feels_like"] - 273.15, 2)
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        sunrise = weather_data["sys"]["sunrise"]
        sunset = weather_data["sys"]["sunset"]

        print(f"Weather in {city_name.title()}: {weather.capitalize()}")  # Title city name and capitalize weather
        # description
        print(f"Country: {country}")
        print(f"Temperature: {temperature} °C (celsius)")
        print(f"Feels_like: {feels_like} °C (celsius)")
        print(f"Humidity: {humidity}%")
        print(f"wind_speed : {wind_speed} m/s")
        print(f"sunrise: {sunrise}")
        print(f"sunset: {sunset}")

        # Offer temperature unit conversion
        unit_choice = input("Would you like to convert to Fahrenheit (F)? (y/n): ")
        if unit_choice.lower() == "y":
            fahrenheit = round(temperature * 9 / 5 + 32, 2)
            print(f"Temperature: {fahrenheit}°F (Fahrenheit)")
    else:
        print("Error fetching weather data. Please check the logs for more details.")


if __name__ == "__main__":
    main()
