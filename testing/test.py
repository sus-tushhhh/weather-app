import json
import httpx
import streamlit as st

url = 'http://api.weatherapi.com/v1/forecast.json'

params = {
    'key' : st.secrets.weather_app.api_key,
    'q' : 'Delhi India',
    'dt' : '2026-03-27',
    'aqi' : 'no'
}

r = httpx.get(url=url, params=params)

with open('test.json', 'w') as f:
    json.dump(r.json(), f, indent=4)

    #hi