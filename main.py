'''The requests library is a powerful tool for interacting with web APIs and web services. It
simplifies the process of making HTTP requests and handling responses.'''
import requests

'''An API key is a unique identifier used to authenticate requests associated with your account. It ensures 
that the requests you make to the OpenWeatherMap API are authorized and can be tracked.'''
API_KEY = "5e756eb1b406ec434b7debcf93457aed"
'''The URL is the endpoint where you can send HTTP requests to get current weather information for 
a specified location'''
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
'''specifies the city for which you want to get the weather data'''
city = input("Enter a city name: ")

# Construct the full URL
'''the requests_url variable constructs the full url by combining BASE_URL, the city name, and the API_KEY'''
url = f"{BASE_URL}?q={city}&appid={API_KEY}"

''' The requests.get() function sends a GET request to the constructed URL. '''
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
else:
    print("An error occurred.")
