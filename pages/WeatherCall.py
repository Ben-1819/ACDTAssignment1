import streamlit as st
import requests
from dotenv import dotenv_values
from loguru import logger

def enterCity():
    st.write("Enter your city")
    
    with st.form("cityEntry"):
        city = st.text_input("Enter your city here")
        submit = st.form_submit_button("Get the weather in your city")
    if not submit:
        st.stop()

    return city

def makeWeatherCall(city):
    apiKeys = dotenv_values(".env")
    # Get the API key
    weatherKey = apiKeys["WEATHER_KEY"]
    # Set the URL
    apiURL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={weatherKey}"

    try:
        response = requests.get(apiURL)
        # Check the HTTP status
        response.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"[ERROR] OpenWeatherMap request failed: {e}")
        return None
    
    return response.json()

def parseWeatherData(data: dict):
    weatherData = data.get("weather")
    cloudsData = data.get("clouds")
    mainData = data.get("main")
    visibility = data.get("visibility")
    windData = data.get("wind")
    cityName = data.get("name")
    st.write(weatherData[0]["main"])
    return {
        "weather": weatherData,
        "clouds": cloudsData,
        "main": mainData,
        "visibility": visibility,
        "wind": windData,
        "city": cityName
    }

def displayWeather(weatherReport):
    st.markdown(f"# Weather report for {weatherReport['city']}")

    with st.expander(f"View report", expanded=False):
        # Show a description of the main weather
        st.write(f"The current weather is {weatherReport['weather'][0]['description']}")
        st.write(f"The current temperature is {weatherReport['main']['temp']} but it feels like {weatherReport['main']['feels_like']}")
        st.write(f"The maximum temperature is {weatherReport['main']['temp_max']} and the minimum temperature is {weatherReport['main']['temp_min']}")
        st.write(f"The visibility is {weatherReport['visibility']} meters")
        st.write(f"Wind speed is {weatherReport['wind']['speed']} mph, wind degrees is {weatherReport['wind']['deg']}")
        st.write(f"Cloud coverage is {weatherReport['clouds']['all']}%")

def main():
    city = enterCity()
    weatherCallData = makeWeatherCall(city)
    weatherReport = parseWeatherData(weatherCallData)
    displayWeather(weatherReport)
main()