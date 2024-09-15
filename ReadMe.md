**OpenWeatherMap Current Weather App**

This Python script fetches current weather information for a specified city using the OpenWeatherMap API.

**Features:**

- Retrieves weather description (e.g., "clear sky", "light rain")
- Calculates and displays temperature in Celsius

**Requirements:**

- Python 3
- `requests` library (install using `pip install requests`)

**Usage:**

1. **Install the `requests` library:**

   ```bash
   pip install requests
   ```

2. **Run the script:**

   ```bash
   python weather.py  # Replace 'weather.py' with your actual file name
   ```

   You'll be prompted to enter a city name.

**Explanation:**

- **Imports:** The script imports the `requests` library for making HTTP requests.
- **API Key:** Replace the placeholder `API_KEY` with your actual OpenWeatherMap API key (obtainable
  from [https://openweathermap.org/](https://openweathermap.org/)).
- **Base URL:** This defines the endpoint for the OpenWeatherMap weather API.
- **City Input:** The script prompts the user to enter a city name.
- **URL Construction:** The `url` variable builds the complete URL by combining the base URL, city name, and API key
  using f-strings for string formatting.
- **Making the Request:** `requests.get(url)` sends a GET request to the constructed URL.
- **Handling Response:**
    - If successful (status code 200), the script parses the JSON response and extracts the weather description and
      temperature.
    - The temperature is converted from Kelvin to Celsius using `round(data["main"]["temp"] - 273.15, 2)`.
    - The extracted data is then printed to the console.
- **Error Handling:** If the request fails, an error message is displayed.

**Additional Notes:**

- Consider adding comments within the code to improve readability and maintainability.
- You can extend the script to display additional weather data like humidity, wind speed,- etc. (refer to the
  OpenWeatherMap API documentation).
- Always use a valid API key and respect the OpenWeatherMap usage limits.

**Disclaimer:** Replace `5e756eb1b406ec434b7debcf93457aed` with your actual API key to avoid exceeding usage limits and
potential issues with the provided key. It's best practice to keep your API key private and not share it publicly.