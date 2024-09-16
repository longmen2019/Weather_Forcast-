# Weather Data Fetcher

This project is a simple Python application that fetches weather data for a given city using the OpenWeatherMap API. It
demonstrates how to make HTTP requests and handle responses using the `requests` library.

## Features

- Fetches current weather data for a specified city.
- Displays weather description and temperature in Celsius.
- Handles errors and provides feedback to the user.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/weather-data-fetcher.git
    cd weather-data-fetcher
    ```

2. Install the required dependencies:
    ```bash
    pip install requests
    ```

## Usage

1. Obtain an API key from OpenWeatherMap.

2. Set your API key as an environment variable:
    ```bash
    export OPENWEATHERMAP_API_KEY='your_api_key_here'
    ```

3. Run the application:
    ```bash
    python weather_fetcher.py
    ```

4. Enter the name of the city when prompted.

## Example

```bash
Enter a city name: London
Weather in London: clear sky
Temperature: 15.32 Celsius
