## Python Weather App - Get Weather Data for Any City

This Python project provides a simple command-line application to retrieve current weather data for any city of your
choice using the OpenWeatherMap API.

**Features:**

* Fetches current weather information including description, temperature, feels like, humidity, wind speed, sunrise, and
  sunset times (in human-readable format).
* Offers conversion between Celsius (°C) and Fahrenheit (°F).
* Utilizes environment variables for secure storage of your API key.
* Employs error handling with informative logs to troubleshoot issues.

**Requirements:**

* Python 3.x
* `requests` library (install using `pip install requests`)
* An OpenWeatherMap API key (get yours from [https://openweathermap.org/api](https://openweathermap.org/api))

**Installation:**

1. Clone this repository or download the files.
2. Install the `requests` library: `pip install requests`

**Usage:**

1. Set your OpenWeatherMap API key in an environment variable named `OPENWEATHERMAP_API_KEY`. Refer to your platform's
   documentation for setting environment variables.
2. Run the script: `python main.py`
3. Enter the name of the city you want weather data for.
4. The script will display the retrieved weather information.
5. (Optional) Choose to convert the temperature to Fahrenheit.

**Example Output:**

```
Enter a city name: London

Weather in London: Cloudy
Country: GB
Temperature: 18.23 °C (celsius)
Feels_like: 17.32 °C (celsius)
Humidity: 78%
Wind_speed: 2.1 m/s
Sunrise: 2024-09-18 06:56:50
Sunset: 2024-09-18 19:22:12

Would you like to convert to Fahrenheit (F)? (y/n): y
Temperature: 64.81°F (Fahrenheit)
```

**Further Enhancements (Optional):**

* Integrate weather icons for a more visual representation.
* Add support for retrieving weather forecasts for multiple days.
* Implement a graphical user interface (GUI) for a more user-friendly experience.

**Contribution:**

Feel free to contribute to this project by creating pull requests with additional features or improvements.
