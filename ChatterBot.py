# Dependencies
import tweepy
import json
import time

#added line to make a new line no reason
# Twitter API Keys
consumer_key = 'sabuUUyKD7AGfaTzurpRGmdYP'
consumer_secret = 'DJTqZcwS74QjkpY9uJ08X6Ahn2eHLCyhuaEwrM0AvDaK5MDXtB'
access_token = '801373896649752576-hW9RPhvqpZ8BCOS0kpZfCwLIulOP7wu'
access_token_secret = 'c5DLoSUDVtAQy2fgyx0WN7pMklIr9UqTENtPXxDWq9FHV'
openweather_api_key = "25bc90a1196e6f153eece0bc0b0fc9eb"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERE