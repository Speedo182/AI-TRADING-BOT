import tweepy
import json
from textblob import TextBlob
from datetime import datetime
import pandas as pd
import time

# Twitter API keys
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Hashtags to search for
hashtags = ['#blockchain', '#bitcoin', '#ethereum', '#shib', '#crypto', '#cryptocurrency']

# Function to search for tweets containing the names of the top 20 coins
def search_top_coins(api, coin_list):
    tweets = []
    for coin in coin_list:
        search_results = api.search(q=coin, lang='en', tweet_mode='extended')
        for tweet in search_results:
            tweets.append(tweet.full_text)
    return tweets

# Function to gather data on sentiment and sentiment changes
def get_sentiment_data(api, hashtags):
    # Dataframe to store sentiment data
    df = pd.DataFrame(columns=['Date', 'Hashtag', 'Sentiment'])
    for hashtag in hashtags:
        search_results = api.search(q=hashtag, lang='en', tweet_mode='extended')
        for tweet in search_results:
            text = tweet.full_text
            date = tweet.created_at
            sentiment = TextBlob(text).sentiment.polarity
            df = df.append({'Date': date, 'Hashtag': hashtag, 'Sentiment': sentiment}, ignore_index=True)
    return df

# Function to gather data on sentiment and sentiment changes for the top 20 coins
def get_coin_sentiment_data(api, coin_list):
    # Dataframe to store sentiment data
    df = pd.DataFrame(columns=['Date', 'Coin', 'Sentiment'])
    for coin in coin_list:
        search_results = api.search(q=coin, lang='en', tweet_mode='extended')
        for tweet in search_results:
            text = tweet.full_text
            date = tweet.created_at
sentiment = TextBlob(text).sentiment.polarity
df = df.append({'Date': date, 'Coin': coin, 'Sentiment': sentiment}, ignore_index=True)
return df
Function to plot sentiment data
def plot_coin_sentiment_data(df, coin_list):
for coin in coin_list:
coin_df = df[df['Coin'] == coin]
sns.lineplot(x='Date', y='Sentiment', data=coin_df)
plt.title(coin + ' Sentiment')
plt.show()

# Function to gather and plot data for all coins in the coin_list
def gather_and_plot_coin_sentiment_data(api, coin_list):
df = get_coin_sentiment_data(api, coin_list)
plot_coin_sentiment_data(df, coin_list)

# Function to gather and plot data for a specific coin
def gather_and_plot_sentiment_data_for_coin(api, coin):
coin_list = [coin]
df = get_coin_sentiment_data(api, coin_list)
plot_coin_sentiment_data(df, coin_list)

# Function to gather and plot data for all coins in the coin_list
def gather_and_plot_coin_sentiment_data(api, coin_list):
df = get_coin_sentiment_data(api, coin_list)
plot_coin_sentiment_data(df, coin_list)

# Function to gather and plot data for a specific coin
def gather_and_plot_sentiment_data_for_coin(api, coin):
coin_list = [coin]
df = get_coin_sentiment_data(api, coin_list)
plot_coin_sentiment_data(df, coin_list)

# Main function to run the twitter bot
def main():
# Authenticate with Twitter
api = authenticate()
# List of coins to gather data for
coin_list = ['Bitcoin', 'Ethereum', 'SHIB', 'Crypto', 'Cryptocurrency']
# Gather and plot data for all coins
gather_and_plot_coin_sentiment_data(api, coin_list)
# Gather and plot data for a specific coin
gather_and_plot_sentiment_data_for_coin(api, 'Bitcoin')

if name == 'main':
main()
