import streamlit as st

st.set_page_config(
    page_title="Home"
)

st.write("ACDT Assignment 1")

st.markdown(
    """
    # CryptoPrice
    Uses a cryptocurrency price API
    # IPCall
    Gets the users location and displays it on a map
    # NewsCall
    Allows the user to choose 1 or 2 keywords and then get 5 news articles containing those keywords
    # WeatherByLocation
    Combined OpenWeatherMap API and ip-api to get the weather in the users current location
    # WeatherCall
    Lets the user enter a city that they want to get the weather for
    """
    )