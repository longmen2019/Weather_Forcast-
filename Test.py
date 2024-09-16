# Key Changes:
# Error Handling: Added try-except blocks to handle HTTP and general errors.
# Configuration: Moved the API key to an environment variable.
# Input Validation: Added a check to ensure the city name is not empty.
# Logging: Configured logging to capture errors and other information.
# These changes should make your code more robust and easier to maintain. Let me know if you need further assistance!
#

import requests
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)


def get_weather_data(city_name, api_key):
    """Fetches weather data for a given city using the OpenWeatherMap API

    Args:
        city_name: The name of the city to get weather data for.
        api_key: Your OpenWeatherMap API key.

    Returns:
        A dictionary containing weather data (or None if an error occurs).
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    url = f"{base_url}?q={city_name}&appid={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
    except Exception as err:
        logging.error(f"An error occurred: {err}")
    return None

def main():
    """Prompts user for city name, fetches weather data, and displays it."""
    api_key = os.getenv("OPENWEATHERMAP_API_KEY", "your_default_api_key_here")
    city_name = input("Enter a city name: ").strip()

    if not city_name:
        print("City name cannot be empty.")
        return

    weather_data = get_weather_data(city_name, api_key)

    if weather_data:
        weather = weather_data["weather"][0]["description"]
        temperature = round(weather_data["main"]["temp"] - 273.15, 2)
        print(f"Weather in {city_name}: {weather}")
        print(f"Temperature: {temperature} Celsius")
    else:
        print("An error occurred while fetching weather data.")

if __name__ == "__main__":
    main()
