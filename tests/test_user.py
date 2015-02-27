import unittest

from .. import auth, api
from ..user import RandomUsers, User

class TestTweepyAPI(unittest.TestCase):

	api = None

	@classmethod
	def setUpClass(cls):
		try:
			from ..config import consumer_key, consumer_secret, access_token, access_token_secret
			tweepy_auth = auth.Authenticate(consumer_key, consumer_secret, access_token, access_token_secret)
			tweepy_auth = tweepy_auth.auth()
		except ImportError as e:
			raise e

		cls.api = api.API(tweepy_auth, retry_count=3, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

class TestRandomUsers(TestTweepyAPI):

	def setUp(self):
		self.assertIsNotNone(self.api, "self.api is None")
		self.random_users = RandomUsers(self.api)
		self.assertIsInstance(self.random_users, RandomUsers)

	def tearDown(self):
		self.random_users = None

	def test_generate_random_id(self):
		random_id = RandomUsers.generate_random_id()
		self.assertLess(random_id, RandomUsers.max_twitter_id)

	def test_generate_random_id_list(self):
		list_length = 20
		random_id_list = RandomUsers.generate_random_id_list(list_length)
		self.assertEqual(list_length, len(random_id_list))
		for random_id in random_id_list:
			self.assertLess(random_id, RandomUsers.max_twitter_id)

	def test_get_random_users(self):
		list_length = 148
		random_users = self.random_users.get_random_users(list_length) 
		self.assertEqual(len(random_users), list_length)
		self.assertGreater(len(random_users), 0)
		for random_user in random_users: 
			self.assertIsInstance(random_user, User)

if __name__ == '__main__':
	unittest.main()
