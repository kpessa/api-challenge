import requests
from api_keys import weather_api_key

class City:
    def __init__(self,name="",lat=0,lng=0,max_temp=0,humidity=0,cloudiness=0, wind_speed=0.0, country="", date=0,response=""):
        self.response = response
        global index
        self.name = name
        self.lat = lat
        self.lng = lng
        self.max_temp = max_temp
        self.humidity = humidity
        self.cloudiness = cloudiness
        self.wind_speed = wind_speed
        self.country = country
        self.date = date

        self.process_api()

    def skipQ(self):
        if self.response['cod']=='404':
            return True
        elif self.response['coord']['lat'] != 0:
            return False

    def process_api(self):
        self.set_response()

        if self.skipQ():
            pass
        else:
            self.store_information() 
    
    def set_response(self):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.name}&appid={weather_api_key}"
        self.response = requests.get(url).json()
        
    def get_response(self):
        if self.response == "":
            self.set_response()
        return self.response

    def store_information(self):
        
        # storing information for the 1st city        
        self.lat = self.response['coord']['lat']
        self.lng = self.response['coord']['lon']
        self.max_temp = self.response['main']['temp_max']
        self.humidity = self.response['main']['humidity']
        self.cloudiness = self.response['clouds']['all']
        self.wind_speed = self.response['wind']['speed']
        self.country = self.response['sys']['country']
        self.date = self.response['dt']
            
            
        