import json
import httpx
import streamlit as st
from datetime import datetime

class Weather:
    def __init__(self, query:str):
        self.url = "http://api.weatherapi.com/v1/forecast.json"
        self.params = {
            'key' : st.secrets.weather_app.api_key,
            'dt'  : datetime.now().date(),
            'q'   : query 
        }
        
    def get_response(self):
        try:
            self.response : dict = httpx.get(url=self.url, params=self.params, timeout=10).json()
        
            if self.response.get('error'):
                return False
            else:
                self.location    : dict = self.response.get('location')
                self.current     : dict = self.response.get('current')
                self.forecast    : dict = self.response.get('forecast')
                self.forecastday : dict = self.forecast.get('forecastday')[0]
                self.today       : dict = self.forecastday.get('day')
                self.astro       : dict = self.forecastday.get('astro')
                self.hourly      : list[dict] = self.forecastday.get('hour')
                return True
                
        except httpx.ConnectTimeout as e:
            return False

        except Exception as e:
            return False



if __name__ == '__main__':
    x = Weather("Delhi")
    if x.get_response():
        for i, j in x.__dict__.items() :
            print(i, j)