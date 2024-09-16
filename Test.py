import requests


def get_weather_data(city_name, api_key):
    """Fetches weather data for a given city using the OpenWeatherMap API.

    Args:
        city_name: The name of the city to get weather data for.
        api_key: Your OpenWeatherMap API key.

    Returns:
        A dictionary containing weather data (or None if an error occurs).
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    url = f"{base_url}?q={city_name}&appid={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None


def main():
    """Prompts user for city name, fetches weather data, and displays it."""
    api_key = "5e756eb1b406ec434b7debcf93457aed"  # Replace with your actual API key
    city_name = input("Enter a city name: ")

    weather_data = get_weather_data(city_name, api_key)

    if weather_data:
        weather = weather_data["weather"][0]["description"]
        temperature = round(weather_data["main"]["temp"] - 273.15, 2)
        print(f"Weather in {city_name}: {weather}")
        print(f"Temperature: {temperature} celsius")
    else:
        print("An error occurred while fetching weather data.")


if __name__ == "__main__":
    main()
