import tweepy

class Authenticate(object):

	def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
		'''
		Sets self.auth to a tweepy.OAuthHandler that authorizes using a Twitter
		consumer key, consumer secret key, access token and access token secret.
		Visit https://apps.twitter.com/ for auth information for your app.
		'''
		self.consumer_key = consumer_key
		self.consumer_secret = consumer_secret
		self.access_token = access_token
		self.access_token_secret = access_token_secret
		
		self.authenticator = tweepy.OAuthHandler(consumer_key, consumer_secret)
		self.authenticator.set_access_token(access_token, access_token_secret)
	

	def auth(self):
		return self.authenticator 
