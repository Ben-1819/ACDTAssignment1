import streamlit as st
import requests
from dotenv import dotenv_values
from loguru import logger

def amountOfKeywords():
    # If keyword amount has been chosen already just continue
    if "keywordNumber" in st.session_state:
        return st.session_state["keywordNumber"]
    
    st.write("How many keywords would you like to search for?")

    with st.form("keywordAmount"):
        amount = st.radio("Keyword amount", ("One", "Two"))
        selectedAmount = st.form_submit_button("Continue")
    if selectedAmount:
        st.session_state["keywordNumber"] = amount
        return amount
    if not selectedAmount:
        st.stop()
    
def oneKeyword():
    # If the keyword has already been chosen then skip this
    if "keyword" in st.session_state:
        return st.session_state["keyword"]
    
    st.write("Enter your keyword below")

    with st.form("oneKeywordInput"):
        keyword = st.text_input("Enter your keyword")
        continueBtn = st.form_submit_button("Continue")
    if continueBtn:
        st.session_state["keyword"] = keyword
        return keyword
    if not continueBtn:
        st.stop()

def twoKeywords():
    # If the keyword has already been chosen then skip this
    if "keyword" in st.session_state:
        return st.session_state["keyword"]
    
    st.write("Enter your two keywords below")

    with st.form("twoKeywordInput"):
        keywordOne = st.text_input("Enter your first keyword")
        keywordTwo = st.text_input("Enter your second keyword")
        continueBtn = st.form_submit_button("Continue")
    if not continueBtn:
        st.stop()
    if keywordOne and keywordTwo:
        # Combine the two keywords into a single string
        keyword = f"{keywordOne}+{keywordTwo}"
        st.session_state["keyword"] = keyword
        return keyword
    else:
        st.warning("Please enter two keywords.")
        st.stop()

def makeNewsCall(query: str):
    apiKeys = dotenv_values(".env")

    apiKey = apiKeys["NEWS_KEY"]
    # Set API URL
    apiUrl = f"https://gnews.io/api/v4/search?q={query}&lang=en&max=5&apikey={apiKey}"
    # Set params
    params = {
        "q": query,
        "lang": "en",
        "max": 5,
        "apiKey": apiKey
    }
    try:
        # Make request
        response = requests.get(apiUrl)
        # Check the status of the response
        response.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"[ERROR] GNews request failed: {e}")
        return None
    return response.json()

def parseNewsCall(data: dict):
    
    articles = data.get('articles', [])
    return articles

def showArticles(articles):
    st.markdown("# Articles")
    if not articles:
        st.markdown("No articles found")
    else:
        # Loop through the articles
        for article in articles:
            # Show the articles title and source
            title = article.get("title", "No title")
            source_name = article.get("source", {}).get("name", "Unknown source")

            with st.expander(f"{title} · {source_name}", expanded=False):
                # Show the articles description if it has one
                if article.get("description"):
                    st.markdown(f"**Summary:** {article['description']}")
                # Show the articles content
                if article.get("content"):
                    st.write(article["content"])
                # Show a url to the articles source
                st.markdown(f"[Read full article]({article['url']})")

# Reset the session state to go again
def resetState():
    resetKeys = ["keywordNumber", "keyword"]
    
    for key in resetKeys:
        if key in st.session_state: del st.session_state[key]

    st.rerun()

def main():
    if st.button("Reset Page"):
        resetState()

    amount = amountOfKeywords()

    if amount == "One":
        keyword = oneKeyword()
    else:
        keyword = twoKeywords()

    news = makeNewsCall(keyword)
    articles = parseNewsCall(news)

    showArticles(articles)
    
main()