import time
import allure
import pytest

from api.vip import VipAPI
from config import BaseDir
from utils import get_case_data

case_data = get_case_data(BaseDir + "/data/test01_vip.json")


# Create test classes

class TestVip:
    # # Define a class-level fixture initialization method
    def setup_class(self):
        self.vip_api = VipAPI()

    @pytest.mark.parametrize("status_code", case_data)
    @allure.story("check vip website")
    def test01_get_vip(self, status_code):
        response = self.vip_api.get_vip()
        print(response)
        # Assert whether the status code is 200
        self.assertEqual(status_code, response.status_code)
