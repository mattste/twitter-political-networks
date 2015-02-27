import random

from tweepy import TweepError

class MissingArgumentError(ValueError):
	pass

class User(object):
	
	def __init__(self, api, screen_name=None, user_id=None):
		self.api = api

		if screen_name is None and user_id is None:
			raise MissingArgumentError("You must provide a screen name or userid")
		
		# set user_id and screen_name, makes API requests for them if not passed to init
		if user_id and screen_name:
			self.user_id = user_id
			self.screen_name = screen_name	
		elif user_id:
			self.screen_name = self.api.get_user(user_id=user_id).screen_name
		else:
			self.user_id = self.api.get_user(screen_name=screen_name).id
		

	def get_friends(self, detailed=False):
		'''
		Returns the Twitter user's first 5,000 friends Twitter user ids.
		If detailed is true, will return full user objects for friends.
		'''
		try:
			if not self.friends:
				self.friends = self.api.friends_ids(id=self.user_id)
			
			# Get detailed information for all friends
			if detailed:
				# implement and test
				# self.api.lookup_users(user_ids=self.friends)
				pass
		except TweepError as e:
			print "Encountered error: %s for user id: %s" % (e, user_id)
			return []

		return self.friends

class RandomUsers(object):

	max_twitter_id = 3000000000

	def __init__(self, api):
		self.api = api

	@classmethod
	def generate_random_id(cls):
		'''
		Returns a random int between 0 and max_twitter_id 
		'''
		return random.randint(0, cls.max_twitter_id)

	@classmethod
	def generate_random_id_list(cls, random_list_length):
		'''
		Returns a list of random integers. Generate a list with a random range
		of numbers between (0-max_twitter_id). Takes random_list_length
		which is the number of random integers to return.
		'''
		random_ids = random.sample(xrange(cls.max_twitter_id), random_list_length)
		return random_ids

	def get_random_users(self, num_users):
		'''
		Gets a list of random twitter users by generating random twitter user_ids
		'''
		# multiply input by 2 since a lot of random nums won't be valid twitter IDs
		random_ids = self.generate_random_id_list(num_users*5)
		random_users = []

		left_index = 0
		right_index = 99

		# get num_users random twitter users
		while len(random_users) < num_users:			
			try:
				lookup = self.api.lookup_users(user_ids=random_ids[left_index:right_index])
				
				# looked up more users than needed
				if len(lookup) + len(random_users) > num_users:
					random_users.extend(lookup[:(num_users-len(random_users))])
				else:
					random_users.extend(lookup)
			except TweepError as e:
				print e

			# out of random ids, so regenerate some more
			if right_index >= len(random_ids):
				random_ids = self.generate_random_id_list((num_users - len(random_users) * 5))


			left_index = right_index
			right_index = left_index + 99

		random_users = [User(api=self.api, screen_name=random_user.screen_name,  user_id=random_user.id) for random_user in random_users]
		return random_users
		




