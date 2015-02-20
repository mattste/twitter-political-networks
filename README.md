# twitter-political-networks
A research project with Julia Kamin on examining the spread of political information via Twitter networks.

## Set-up

Install the dependencies:
```pip install -r requirements.txt```

Verify you have a Twitter app set-up. Visit [https://apps.twitter.com/] for auth information for your app.

Create your config.py file that has the following values:
```
consumer_key = 'consumer key here'
consumer_secret = 'consumer secret here'

access_token = 'access token here'
access_token_secret = 'access token secret here'
```

## Run a script

### Authenticate

Add these lines to your code to handle authentication and create an api object that you can work with:
```
try:
	from config import consumer_key, consumer_secret, access_token, access_token_secret
	auth = Authenticate(consumer_key, consumer_secret, access_token, access_token_secret)
	auth = auth.auth()
except ImportError as e:
	raise e

api = API(auth, retry_count=3, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
```

Pass the api object to the class you'll be working with, such as in our snowball:
```
sb = Snowball(api)
```