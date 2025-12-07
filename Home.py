import streamlit as st

st.set_page_config(
    page_title="Home"
)

st.write("ACDT Assignment 1")

st.markdown(
    """
    # Home Page
    Use the sidebar for navigation to use the APIs straight away or read below for a quick list of APIs used and the data they will return
    
    ## List of APIs used:
    - api-ninjas crypto price
    - IP-API
    - GNews
    - OpenWeatherMap
    
    ## Crypto Price API
    The first API being used is api-ninjas crypto price
    
    The api-ninjas crypto price API free tier allows retrieval of the current value of a cryptocurrency based off the symbol used
    
    ### Parameters
    There is only one parameter required and that is the symbols header, the symbol that will be put in the parameter will be selected from a dropdown, but because the CryptoSymbols API is premium only I will not be adding all available crypto symbols.
    
    ### Headers
    There is one header that is required with this API and that is the X-Api-Key header, it will be filled in automatically using the CRYPTO_KEY variable from the environment file
    ### Response
    There are three fields returned in the response:
    - Symbol
        - The cryptocurrency trading pair symbol that data is being retrieved for
    - Price
        - The current price of the cryptocurrency trading pair
    - Timestamp
        - The timestamp of the price (unix)

    ## IP-API
    The second API being used is ip-api
    
    ip-api is an API for geolocation using IP addresses, I am getting the IP addresses using the FindMyIp package
    
    ### Parameters
    There are three optional parameters that can be used with this API:
    - fields
    - lang
    - callback
    The only parameter I will be using is fields because I don't want to retrieve more fields than necessary.
    There is no API key required to use this API
    
    ### Returned Fields
    I am only going to be retrieving these fields, but there is many more that could be retrieved
    - Status
        - If the request was a success or a fail
    - Message
        - Only included if the request fails, allows for more information on why it failed
    - Country
        - The country that the ip address is in
    - City
        - The city the ip address is in
    - Lat
        - The Latitude 
    - Lon
        - The Longitude
    - Timezone
        - The timezone the ip address is in

    ## GNews
    The third API being used is GNews
    
    GNews is an API that lets the user retrieve news articles, they are searched by keyword which is the only required parameter
    
    ### Parameters
    There are a lot of query parameters with this API so I will list the ones being used by me
    - q (Required)
        - Allows you to specify keywords to search for
    - lang
        - Specifies the language of the news articles being returned by the API, use 2 letter language codes
    - max
        - Specifies the maximum amount of articles to be returned
    - sortby
        - Allows you to sort the returned articles by either publication date or by relevance
    
    The API key is also sent in the parameters, it is in the environment file under the NEWS_KEY variable

    ### Response
    The articles are returned in a json response as follows (none of these values are real, just for example purposes):
    ``` 
    {
        "totalArticles": 5
        "articles":[
            {
                "id": "abdc1",
                "title": "Example title",
                "description": "Example description",
                "content": "Example content",
                "url": "https://exampleNewsSite.com",
                "image": "https://exampleUrlToImage",
                "publishedAt": "2025-09-30T19:38:25Z",
                "lang": "en",
                "source":{
                    "id": "abcdef1728",
                    "name": "exampleNewsSite",
                    "url": "https://exampleNewsSite.com",
                    "country": "us"
                }
            }  
        ]
    }
    ```
    #### Explanation of response fields:
    - id
        - Unique identifier for the article
    - title
        - The title of the article
    - description
        - The description of the article
    - content
        - The content of the article, premium users are shown the full content of the article but for users on the free plan it is truncated
    - url
        - A url to the article
    - image
        - The main image of the article
    - publishedAt
        - Date of the publication of the article (UTC)
    - lang
        - The language of the article
    - source.id
        - Unique identifier for the source of the article (News site the published it)
    - source.name
        - Name of the source
    - source.url
        - Homepage of the source
    - source.country
        - The country that the source is based in
    
    ## OpenWeatherMap
    The fourth API being used is OpenWeatherMap

    It returns the current weather in the users area, it will be called in two different scripts, one where OpenWeatherMap is by itself and the user inputs their city, in the second it is compined with ip-api to get the users lat and lon to automatically show them the weather where they are

    ### Parameters
    - city (required unless using lat & long)
        - The city the user is searching the weather in
    - lat (required unless using city)
        - The latitude the user is searching for
    - lon (required unless using city)
        - The longitude the user is searching for
    - units
        - The measurement system being used for the units
    - appkey
        - the API key
    
    I am storing the API key in the environment file under the variable WEATHER_KEY

    ### Response
    This is the structure of the json response (example data): 

    ```
    {
        "coord": {
            "lat": 1,
            "lon": 1
        },
        "weather": [
            {
                "id": 1,
                "main": "Rain",
                "description": "heavy intensity rain",
                "icon": "10d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 9.83,
            "feels_like": 7.98,
            "temp_min": 9.5,
            "temp_max": 10.12,
            "pressure": 989,
            "humidity": 97,
            "sea_level": 989,
            "grnd_level": 978
        },
        "visibility": 1800, 
        "wind": {
            "speed": 3.6, 
            "deg": 210
        }, 
        "rain": {
            "1h": 1.75
        }, 
        "clouds": {
            "all": 100
        }, 
        "dt": 1765117070, 
        "sys": {
            "type": 1, 
            "id": 1376, 
            "country": "GB", 
            "sunrise": 1765096285, 
            "sunset": 1765123211
        }, 
        "timezone": 0, 
        "id": 2644411, 
        "name": "cityName", 
        "cod": 200
    }
    ```

    #### Explanation of response fields
    There are a lot of response fields so this list only contains the important ones
    1. coord.lat
        - Latitude
    2. coord.lon
        - Longitude 
    3. weather.id
        - Weather type id
    4. weather.main
        - Main weather
    5. weather.description
        - More in depth description of weather
    6. weather.icon
        - Icon for the current weather
    7. main.temp
        - Actual temperature
    8. main.feels_like
        - What the temperature feels like
    9. main.temp_min
        - The minimum temperature
    10. main.temp_max
        - The maximum temperature
    11. main.pressure
        - The air pressure
    12. visibility
        - Visibility 
    13. wind.speed
        - Wind speed
    14. wind.direction
        - Wind direction in degrees
    15. rain.1h
        - Amount of rainfall per hour (mm)
    16. clouds.all
        - Cloud coverage
    """
    )