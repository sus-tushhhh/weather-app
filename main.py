import streamlit as st
import json
from cogs.weather_api import Weather

st.set_page_config(page_title='Weather Lens', layout='wide')
st.title('🌦️ Weather Lens | Forecast at a Glance')
st.subheader('In Development')


def get_base_locations():
    with open('base_locations.json', 'r') as f:
        return json.load(f)


st.selectbox(
    label    ='Enter a city, state or country',
    options  = get_base_locations(),
)