import pandas as pd
import pathway as pw
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Path to your financial news dataset
dataset_path = os.environ.get("FINANCIAL_NEWS_DATASET_LOCAL_PATH", "/path/to/financial_news.csv")

def run(host, port):
    user_input, response_writer = pw.io.http.rest_connector(
        host=host,
        port=port,
        schema=UserInputSchema,
        autocommit_duration_ms=50,
    )

    sentiment = analyze_sentiment(user_input) 

    formatted_response = format_sentiment(sentiment)  

    response_writer(formatted_response)  

    pw.run()

class UserInputSchema(pw.Schema):
    query: str

def analyze_sentiment(user_input):
    
    financial_news_df = pd.read_csv(dataset_path)

    sentiment = "Positive"

    return sentiment

def format_sentiment(sentiment):
    formatted_response = f"Sentiment: {sentiment}\n"
    return formatted_response

if __name__ == "__main__":
    run("localhost", 8080)
