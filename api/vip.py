import requests


# Create interface classes
class VipAPI:
    def __init__(self):
        # Define the domain name
        BASE_URL = "http://www.baidu.com"
        # Define the path
        self.url_vip = BASE_URL

    # Send a request of "the 9-Day forecast"
    def get_vip(self):
        return requests.get(url=self.url_vip)

