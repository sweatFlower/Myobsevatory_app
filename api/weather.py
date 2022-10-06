import requests


# Create interface classes
class WeatherAPI:
    def __init__(self):
        # Define the domain name
        BASE_URL = "https://www.hko.gov.hk"
        # Define the path
        self.url_weather_9dayforecast = BASE_URL + "/wxinfo/currwx/climatjs/9day1006_1014.js"

    # Send a request of "the 9-Day forecast"
    def get_weather_9dayforecast(self, current_time):
        return requests.get(url=self.url_weather_9dayforecast,params=current_time)

