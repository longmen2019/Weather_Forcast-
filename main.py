'''The requests library is a powerful tool for interacting with web APIs and web services. It
simplifies the process of making HTTP requests and handling responses.'''
import requests


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

    ''' The requests.get() function sends a GET request to the constructed URL. '''
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None


def main():
    """Prompts user for city name, fetches weather data, and displays it."""

    """An API key is a unique identifier used to authenticate requests associated with your account. It ensures
    that the requests you make to the OpenWeatherMap API are authorized and can be tracked."""
    api_key = "5e756eb1b406ec434b7debcf93457aed"

    """specifies the city for which you want to get the weather data"""
    city_name = input("Enter a city name: ")

    weather_data = get_weather_data(city_name, api_key)

    # Check if the request was successful
    if weather_data:
        weather = weather_data["weather"][0]["description"]
        temperature = round(weather_data["main"]["temp"] - 273.15, 2)
        print(f"Weather in {city_name}: {weather}")
        print(f"Temperature: {temperature} celsius")
    else:
        print("A error occurred while fetching weather data.")


if __name__ == "__main__":
    main()
