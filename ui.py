import os
import streamlit as st
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_host = os.environ.get("HOST", "localhost")
api_port = int(os.environ.get("PORT", 8080))


# Streamlit UI elements
st.title("Financial News Sentiment Analysis")

news_query = st.text_input(
    "Enter a query",
    placeholder="e.g., stock market, company name"
)

if st.button("Analyze Sentiment"):
    if news_query:
        url = f'http://{api_host}:{api_port}/'
        data = {"query": news_query}

        response = requests.post(url, json=data)

        if response.status_code == 200:
            sentiment = response.json().get("sentiment", "N/A")
            st.write(f"### Sentiment Analysis Result:")
            st.write(f"The sentiment for '{news_query}' is: {sentiment}")
        else:
            st.error(f"Failed to analyze sentiment. Status code: {response.status_code}")
