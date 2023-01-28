import requests
import json
import pandas as pd
from textblob import TextBlob
import tweepy
import praw
import facebook

def scrape_twitter():
    # Twitter API credentials
    consumer_key = "YOUR_CONSUMER_KEY"
    consumer_secret = "YOUR_CONSUMER_SECRET"
    access_token = "YOUR_ACCESS_TOKEN"
    access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

    # authorize the API using the credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # create an empty list to store the tweets
    tweets = []

    # search for tweets containing the specified keywords
    query = "crypto OR cryptocurrency"
    for tweet in tweepy.Cursor(api.search_tweets, q=query, lang="en").items(1000):
        tweets.append(tweet.text)

    return tweets

def scrape_reddit():
    # Reddit API credentials
import requests
import json
import pandas as pd
from textblob import TextBlob
import tweepy
import praw
import facebook

def scrape_twitter():
    # Twitter API credentials
    consumer_key = "YOUR_CONSUMER_KEY"
    consumer_secret = "YOUR_CONSUMER_SECRET"
    access_token = "YOUR_ACCESS_TOKEN"
    access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

    # authorize the API using the credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # create an empty list to store the tweets
    tweets = []

    # search for tweets containing the specified keywords
    query = "crypto OR cryptocurrency"
    for tweet in tweepy.Cursor(api.search_tweets, q=query, lang="en").items(1000):
        tweets.append(tweet.text)

    return tweets

def scrape_reddit():
    # Reddit API credentials
