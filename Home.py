import streamlit as st

st.set_page_config(
    page_title="Home"
)

st.write("ACDT Assignment 1")

st.markdown(
    """
    # CryptoPrice
    Uses a cryptocurrency price API. This is useful to a business that may need access to fast, accurate data such as companies that monitor cryptocurrency markets. Real time pricing allows companies to make better informed decisions.
    # IPCall
    Gets the users location and displays it on a map. This is useful in a business use case as it allows businesses to automatically determine a user's geographical location and personalise services to them or monitor where their users are from
    # NewsCall
    Allows the user to choose 1 or 2 keywords and then get 5 news articles containing those keywords. Can be used in a business use case by allowing organisations to monitor relevant news to their industry such as information on new technologies or events that may impact them
    # WeatherByLocation
    Combined OpenWeatherMap API and ip-api to get the weather in the users current location
    # WeatherCall
    Lets the user enter a city that they want to get the weather for - Provides up to date weather information which can be used for a variety of different things such as field work planning or delivery route monitoring 
    """
    )