import streamlit as st
import requests
from dotenv import dotenv_values
from loguru import logger
import FindMyIP

def getUsersIp():
    usersIp = FindMyIP.external()
    return usersIp

def getIpApiResponse(ip):
    response = requests.get(f"http://ip-api.com/json/{ip}")
    data = response.json()
    return data

def parseIpApiResponse(data: dict):
    userLat = data.get("lat")
    userLon = data.get("lon")

    return{
        "lat": userLat,
        "lon": userLon
    }

def checkConnectionStatus():
    connectionStatus = FindMyIP.internet()
    return connectionStatus


def makeWeatherCall(lat, lon):
    apiKeys = dotenv_values(".env")
    # Get the API key
    weatherKey = apiKeys["WEATHER_KEY"]
    # Set the URL
    apiURL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={weatherKey}"

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
    userConnection = checkConnectionStatus()

    if(userConnection != True):
        #logger.error("The user is not connected to the internet")
        st.write("You are not connected to the internet")
        st.stop()

    ipAddress = getUsersIp()

    ipInformation = getIpApiResponse(ipAddress)
    locationInformation = parseIpApiResponse(ipInformation)    
    weatherCallData = makeWeatherCall(locationInformation['lat'], locationInformation['lon'])
    weatherReport = parseWeatherData(weatherCallData)
    displayWeather(weatherReport)
main()