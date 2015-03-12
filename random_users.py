from auth import Authenticate
from api import API
from user import User, RandomUsers

import pandas

try:
	from config import consumer_key, consumer_secret, access_token, access_token_secret
	auth = Authenticate(consumer_key, consumer_secret, access_token, access_token_secret)
	auth = auth.auth()
except ImportError as e:
	raise e

api = API(auth, retry_count=3, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Random Users
ru = RandomUsers(api)


for i in range(0,1):

	random_users = ru.get_random_users(num_users=50)
	random_users_list = []
	for user in random_users:
		friends = user.get_friends()

		# get news handles

		random_users_list.append([user.screen_name, user.user_id, friends])

	print random_users_list

	df2 = pandas.DataFrame(random_users_list)
	df2.columns = ['screen_name', 'id', 'friends']
	df2.to_csv('data/random_users%d.csv', i)
