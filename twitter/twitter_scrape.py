''' twitter_scrape.py
* ====================================================================================
* Name: Zachary Benson, Jan 2022
* Project: OSINT Pipeline
* Purpose: This file contains the functionality to scrape twitter.
* Contact Information: 
*     Email: zachary.n.benson@gmail.com
* ===================================================================================== 
'''
#Dependecies
from twitter.twitter_api_config import *
from twitter.twitter_api_utils import *
import tweepy
import pandas as pd
import requests


def download_image(df):
    #Get the all the tweets that contain media keys.
    df_media = df[df['attachments.media_keys'].notna()]

    #Initialize the download function
    initilize_download()

    #Iterate through every tweet and download images.
    df_media.apply(lambda x: download(x), axis = 1)

    #Clean up the folders.
    clean_up()

def scrape():
    # You can provide the consumer key and secret with the access token and access
    #token secret to authenticate as a user
    client = tweepy.Client(
                            bearer_token=BEARER_TOKEN,
                            consumer_key=CONSUMER_KEY, 
                            consumer_secret=CONSUMER_SECRET, 
                            access_token=ACCESS_TOKEN, 
                            access_token_secret=ACCESS_TOKEN_SECRET, 
                            return_type = requests.Response,
                            wait_on_rate_limit=True)


    # Define query
    query = '#shipsinpics OR #ships OR #shipspotting'
    expansions = ['attachments.media_keys']
    media_fields = ['media_key']

    # Replace with your own search query
    tweets = client.search_recent_tweets(query=query, 
                                               tweet_fields=['context_annotations','created_at','entities'],
                                        media_fields=media_fields, 
                                        expansions=expansions,
                                        max_results=100)

    #Convert the tweets to dataframe.
    df = tweets_to_df(tweets)

    return df

def main():
    df = scrape()
    return df

if __name__ == "__main__":
        main()