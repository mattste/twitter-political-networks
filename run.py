import tweepy

from config import *
from api import API


def authenticate():
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	return auth

auth = authenticate()
api = API(auth)

