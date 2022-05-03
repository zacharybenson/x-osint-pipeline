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
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAJW2bQEAAAAACclZTGo4wYHKzxDXkgRp8HYZ9dM%3Dge0dhuWBlrgL0ISArWKEX9xZc0QgQ85YT5zBJ0lErOB6WnVEgw"

# Your app's API/consumer key and secret can be found under the Consumer Keys
# section of the Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
CONSUMER_KEY = "UF0mpgeFiGcdX69B5gf89UWoz"
CONSUMER_SECRET = "He6pUvaiNm3MfZuo0LIdBrieew1HGoXvaiMPBCOmdFU2n5sOEL"

# Your account's (the app owner's account's) access token and secret for your
# app can be found under the Authentication Tokens section of the
# Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
ACCESS_TOKEN = "787530627708968960-mUpJ5J11J6KBIohkuxTYNA0yYPpcR5n"
ACCESS_TOKEN_SECRET = "ZAxI5Y4rJS4haumjZOxfpVHQrAJ58QeIDLoBAxseuuXxo"

def main():
    return BEARER_TOKEN, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

if __name__ == "__main__":
    main()
