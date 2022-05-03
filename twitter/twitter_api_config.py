''' twitter_api_config.py
* ====================================================================================
* Name: Zachary Benson, Jan 2022
* Project: OSINT Pipeline
* Purpose: This file configures endpoint settings for the twitter api.
* Contact Information: 
*     Email: zachary.n.benson@gmail.com
* ===================================================================================== 
'''
# Your app's bearer token can be found under the Authentication Tokens section
# of the Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
BEARER_TOKEN = ""

# Your app's API/consumer key and secret can be found under the Consumer Keys
# section of the Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
CONSUMER_KEY = ""
CONSUMER_SECRET = ""

# Your account's (the app owner's account's) access token and secret for your
# app can be found under the Authentication Tokens section of the
# Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

def main():
    return BEARER_TOKEN, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

if __name__ == "__main__":
    main()
