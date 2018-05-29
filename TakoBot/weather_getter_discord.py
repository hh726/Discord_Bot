'''
Created on Dec 14, 2017
@author: henry
'''
import urllib.parse
import requests
import key
class Coordinates(object):
    def __init__(self, address):
        self.address = address
        self.location_api = 'http://maps.googleapis.com/maps/api/geocode/json?' + urllib.parse.urlencode({'address': self.address})
        self.location_data = requests.get(self.location_api).json()
    @property
    def get_lat(self):
        return self.location_data['results'][0]['geometry']['location']['lat']
    
    @property
    def get_lon(self): 
        return self.location_data['results'][0]['geometry']['location']['lng']
    def __str__(self):
        if self.location_data['status'] != 'OK':
            return "Location not found"
        return "Location: " + self.location_data['results'][0]['formatted_address']
class Weather(object):
    def __init__(self, lat, lon, key=key.Weather):
        self.lat = lat
        self.lon = lon
        self.key = key
        
        self.weather_api = 'http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&APPID=%s&units=imperial' %(self.lat,self.lon,self.key)
        self.weather_data = requests.get(self.weather_api).json()
        
    def __str__(self):
        detail = """    Temperature : {} Degrees F
    Wind Speed  : {} mph
    Description : {}
    """.format(
            self.weather_data['main']['temp'] ,\
            self.weather_data['wind']['speed'],\
            self.weather_data['weather'][0]['description'])
        return detail

if __name__ == '__main__':
    location = Coordinates(input("Enter a location: "))
    print(location)
    print(Weather(location.get_lat, location.get_lon))