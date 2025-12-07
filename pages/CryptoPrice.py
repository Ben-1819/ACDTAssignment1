import streamlit as st
import requests
from dotenv import dotenv_values
from loguru import logger

# Choose the Cryptocurrency symbol that will have its value shown
def chooseSymbol():
    # Dictionary containing different cryptocurrency symbols and their names
    coinOptions = {
        "Bitcoin": "BTC",
        "Ethereum": "ETH",
        "Binance": "BNB",
        "Ripple": "XRP",
        "Litecoin": "LTC",
        "TRON": "TRX"
    }
    
    # Using a form 
    with st.form("symbolForm"):
        # Show the keys in coinOptions so that it is easily readable for humans
        option = st.selectbox(f"What cryptocurrency do you want to search", coinOptions.keys())

        # Once the user has selected an option search for the value matching the key in
        # The coinOptions dict
        selectedOption = coinOptions[option]

        # Button to submit the form and send the request
        valueChosen = st.form_submit_button("Get value of selected coin")

    # Once the user clicks the button
    if valueChosen:
        #logger.debug(f"Currency selected: {selectedOption}")
        return selectedOption
    
    # If the user has not clicked the button to return their selected symbol
    # Stop running the script past this point or else API call fails
    if not valueChosen:
        st.stop()

# Make the API call
def makeCryptoCall(symbol: str):
    apiKeys = dotenv_values(".env")
    # Get the key for this api from .env
    apiKey = apiKeys['CRYPTO_KEY']
    # Set the api URL
    apiUrl = f'https://api.api-ninjas.com/v1/cryptoprice?symbol={symbol}USD'
    try:
        # Make a get request to the API, pass in the key in the headers section
        response = requests.get(apiUrl, headers={'X-Api-Key': f'{apiKey}'})

        # Check if the request was successful
        response.raise_for_status()

    except requests.RequestException as e:
        # Log error is something goes wrong
        logger.error(f"[ERROR] Crypto price request failed: {e}")
        # Show user there is an error
        st.write(f"Something went wrong: {e}")
        # Stop the script
        st.stop()
    # Return the API response
    return response.json()

# Get the important data from the response
def parseCryptoCall(data: dict):
    # logger.info(f"Data returned from the API: {data}")

    # Retrieve the price from the API response
    price = data.get('price')
    # Retrieve the time from the API response
    time = data.get('timestamp')

    # Return the data
    return {
        "price": price,
        "time": time
    }

# Show the data to the user
def showData(coinInformation: dict):
    st.write(f"Price (USD): ${coinInformation.get('price')}")
    st.write(f"Time: {coinInformation.get('time')}")

# Main function
def main():
    # Call chooseSymbol to let the user select a crypto pair symbol
    symbol = chooseSymbol()

    #logger.debug(f"Symbol: {symbol}")

    # Make the API call
    data = makeCryptoCall(symbol)

    # Get the data from the API call
    coinInformation = parseCryptoCall(data)

    # Show the user the data from the API call
    showData(coinInformation)

main()
#makeCryptoCall("ETHUSD")