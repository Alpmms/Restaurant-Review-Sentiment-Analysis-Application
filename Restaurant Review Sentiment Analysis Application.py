#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import json
from nltk.sentiment import SentimentIntensityAnalyzer
import re
import string
import nltk

YELP_API_KEY = "your_yelp_api_key_here"
YELP_API_URL = "https://api.yelp.com/v3/businesses/search"

def get_yelp_business_data(business_name):
    query_url = f"{YELP_API_URL}?term={business_name}"
    headers = {
        "Authorization": f"Bearer {YELP_API_KEY}"
    }
    response = requests.get(query_url, headers=headers)
    if response.status_code != 200:
        print("Error: Unable to fetch data from Yelp API.")
        sys.exit()
    data = response.json()
    return data

def process_yelp_data(data):
    businesses = data["businesses"]
    if not businesses:
        print("Error: No matching restaurants found.")
        sys.exit()
    business = businesses[0]
    business_name = business["name"]
    review_count = business["review_count"]
    if review_count == 0:
        print(f"{business_name} has no reviews.")
        sys.exit()
    reviews_url = business["review_url"]
    return business_name, reviews_url

def fetch_reviews(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Error: Unable to fetch reviews from the provided URL.")
        sys.exit()
    data = response.text
    return data

def preprocess_reviews(data):
    soup = BeautifulSoup(data, "html.parser")
    reviews = []
    for review in soup.find_all("div", class_="review-container"):
        text = review.find("p", class_="lemon--p__37cl1 p-review-content__3K1fZ margin-b5__3M-tS").text
        reviews.append(text)
    return reviews

def analyze_sentiment(reviews):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = []
    for review in reviews:
        score = sia.polarity_scores(review)
        sentiment_scores.append(score)
    return sentiment_scores

def display_sentiment_info(sentiment_scores):
    total_polarity = 0
    total_words = 0
    for score


# In[ ]:




