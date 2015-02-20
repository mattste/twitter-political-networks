from random import sample
from collections import deque

import pandas
from tweepy.error import TweepError

class Snowball(object):

	def __init__(self, api):
		self.api = api

	def run(self, seed_user_screen_name, num_friends_to_examine, num_rounds):
		'''
		Snowball!
		Returns an edge list that consists of a source_id->friend_id mapping
		'''

		queue = deque()
		edge_list = [] # tuple of (source_id, friend_id)

		root_user = self.api.get_user(id=seed_user_screen_name)
		queue.append(root_user.id)

		# total # nodes = (branch width^depth) - 1
		max_nodes = (num_friends_to_examine**num_rounds)-1
		curr_num_nodes = 1

		# Breadth first tree/network creation
		while curr_num_nodes < max_nodes:

			u = queue.popleft()

			friends = self.get_friends(u)
			random_ints = self.generate_random_int_list(len(friends), num_friends_to_examine)

			for random_int in random_ints:
				friend = friends[random_int]
				edge_list.append((u, friend))
				queue.append(friend)
				curr_num_nodes = curr_num_nodes + 1

		return edge_list

	def export_edges_to_csv(self, edge_list, filename):
		'''
		Takes an edge list and exports it as a csv to filename with columns 'source' and 'target'
		'''
		df = pandas.DataFrame(edge_list)
		df.columns = ['source', 'target']
		df.to_csv(filename)

	def get_friends(self, user_id):
		'''
		Given a Twitter user's id,
		returns the Twitter user id's first 5,000 friends Twitter user ids
		'''
		try:
			friends = self.api.friends_ids(id=user_id)
		except TweepError as e:
			print "Encountered error: %s for user id: %s" % (e, user_id)
			return []
		return friends

	@staticmethod
	def generate_random_int_list(max_length, random_list_length):
		'''
		Returns a list of random integers. Takes max_length which is a the highest number
		that the random range numbers can reach (0-max_length). Takes random_list_length
		which is the number of random integers to return.
		'''
		# highest value for max random integer exceeds the list length
		if max_length < random_list_length:
			random_list_length = max_length

		random_ints = sample(xrange(max_length), random_list_length)
		return random_ints