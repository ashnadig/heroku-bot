# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "Z2cqYyXP4H75UgXffeuvySieO"
consumer_secret = "itU9pU0hnh6xGAK3tUyoEvoISArQhlEGi20wOsxItt76LIOrt6"
access_token = "139497969-D6VsxXP1hplSUlJJSkCUB6VvEdMZtiDVvwGOHAov"
access_token_secret = "L9Txka5njdPQnOfs9Ts6czI36EwADHODli0Iws82ai9bM"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERE