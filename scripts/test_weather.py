import time
import allure
import pytest

from api.weather import WeatherAPI
from config import BaseDir
from utils import get_case_data

case_data = get_case_data(BaseDir + "/data/weather_after_tomorrow.json")


# Create test classes
@pytest.mark.run(order=1)
class TestWeather:
    # # Define a class-level fixture initialization method
    def setUp(self):
        self.weather_api = WeatherAPI()

    @pytest.mark.parametrize("username, code, expect", case_data)
    @allure.story("Check the weather for day after tomorrow")
    def test01_get_weather_9dayforecast(self, status_code):
        # Obtain the current time, 13-bit timestamp
        current_time = {
            "_": int(time.time()*1000)
        }
        # Obtain the response result
        response = self.weather_api.get_weather_9dayforecast(current_time)
        print(response.json())
        # Assert whether the status code is 200
        self.assertEqual(status_code, response.status_code)
        # I'm sorry for lacking knowledge of calculating relative humidity, so I tried my own way
        min_humidity = response.json().get("climat").get("day2").get("minRH")
        max_humidity = response.json().get("climat").get("day2").get("maxRH")
        print("The relative humidity for the day after tomorrow is：{}% - {}%").format(min_humidity, max_humidity)

