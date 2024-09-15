'''The requests library is a powerful tool for interacting with web APIs and web services. It
simplifies the process of making HTTP requests and handling responses.'''
import requests

'''An API key is a unique identifier used to authenticate requests associated with your account. It ensures 
that the requests you make to the OpenWeatherMap API are authorized and can be tracked.'''

API_KEY = "5e756eb1b406ec434b7debcf93457aed"
'''The URL is the endpoint where you can send HTTP requests to get current weather information for 
a specified location'''
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
requests_url = f"{BASE_URL}appid={API_KEY}&Q={city}"
# requests_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
response = requests.get(requests_url)