from auth import Authenticate
from api import API
from snowball import Snowball

try:
	from config import consumer_key, consumer_secret, access_token, access_token_secret
	auth = Authenticate(consumer_key, consumer_secret, access_token, access_token_secret)
	auth = auth.auth()
except ImportError as e:
	raise e

api = API(auth, retry_count=3, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Snowball
sb = Snowball(api)
seed_user_screen_name = 'matt_stewart_'
edge_list = sb.run(seed_user_screen_name=seed_user_screen_name, num_friends_to_examine=10, num_rounds=3)
sb.export_edges_to_csv(edge_list=edge_list, filename='edge_list.csv')


