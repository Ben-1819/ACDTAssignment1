import streamlit as st
import numpy as np
import pandas as pd
import requests
import FindMyIP
from loguru import logger

# Put a title on the screen
def streamlitTitle():
    # Tell the user what this page does
    st.write("Find your location based off IP address")
    # Use a form to stop the script from running everything until the user clicks the button
    with st.form("waitForClick"):
        # Submit button will set buttonClicked to true when clicked
        buttonClicked = st.form_submit_button("Locate me")
    # If buttonClicked isn't true st.stop will stop the script from continuing to run
    if not buttonClicked:
        st.stop()

# Uses the FindMyIP package to get the users IP and then returns it
def getExternalIp():
    userIp = FindMyIP.external()
    st.write(f"Your external IP address is: {userIp}")

    return userIp

# Check the users connection status, if they aren't connected to the internet it wont work
def checkConnectionStatus():
    connectionStatus = FindMyIP.internet()
    return connectionStatus

# Makes the api call to
def makeIpApiCall(ip):
    # Set the api request URL
    apiUrl = f"http://ip-api.com/json/{ip}"
    try:
        # Make a GET request to the api URL
        response = requests.get(apiUrl)
        # Check the HTTP status of the response
        response.raise_for_status()
    except requests.RequestException as e:
        # Log error is something goes wrong
        logger.error(f"[ERROR] ip-api request failed: {e}")
        # Show user there is an error
        st.write(f"Something went wrong: {e}")
        # Stop the script
        st.stop()

    # Return the data from the response in JSON format
    return response.json()

# Gets the data from the response and returns it
def parseApiCall(data: dict):
    # Set userCountry to the country returned in the API response
    userCountry = data.get("country")
    # set userCity to the city returned in the API response
    userCity = data.get("city")
    # set userLat to the lat returned in the API response
    userLat = data.get("lat")
    # set userLon to the lon returned in the API response
    userLon = data.get("lon")

    return {
        "country": userCountry,
        "city": userCity,
        "lat": userLat,
        "lon": userLon,
    }

# Tells the user their country and city
def streamlitWriteLocation(userInfo: dict):
    st.write(f"The country you live in is: {userInfo['country']}")
    st.write(f"And the city you live in is: {userInfo['city']}")

# Shows where the user is on a map
def showMap(userInfo: dict):
    mapData = pd.DataFrame([[userInfo['lat'], userInfo['lon']]], columns=['lat', 'lon'])
    st.map(mapData)

def main():
    streamlitTitle()

    userConnection = checkConnectionStatus()

    if(userConnection != True):
        #logger.error("The user is not connected to the internet")
        st.write("You are not connected to the internet")
        st.stop()

    ipAddress = getExternalIp()

    ipInformation = makeIpApiCall(ipAddress)
    locationInformation = parseApiCall(ipInformation)

    streamlitWriteLocation(locationInformation)

    showMap(locationInformation)


main()