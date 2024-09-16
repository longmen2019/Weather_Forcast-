# Weather Data Fetcher

The Weather Data Fetcher is a Python script that uses the `requests` library to interact with the OpenWeatherMap API. It
fetches and displays current weather data for a specified city.

## Features

- Fetches current weather data for a specified city.
- Displays weather description and temperature in Celsius.
- Offers temperature conversion to Fahrenheit.
- Logs errors and important information.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/weather-data-fetcher.git
    cd weather-data-fetcher
    ```

2. Install the required libraries:
    ```bash
    pip install requests
    ```

3. Set up your OpenWeatherMap API key:
   - Sign up at OpenWeatherMap to get your API key.
   - Set the API key as an environment variable:
       ```bash
       export OPENWEATHERMAP_API_KEY='your_api_key_here'
       ```

## Usage

1. Run the script:
    ```bash
    python weather_fetcher.py
    ```

2. Enter the name of the city when prompted.

3. The script will display the current weather description and temperature in Celsius. You will also have the option to
   convert the temperature to Fahrenheit.