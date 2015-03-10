'''
to sign on to twitter api run the loggingin.py - ie "python loggingin.py" in bash shell
'''
import twitter
import oauthDance
import json
import unicodedata
import pandas
import time
import random

# authorize into twitter api

t = oauthDance.login()

# get list of fox followers

fox_followers = t.followers.ids(screen_name='foxnews',count=2)
fox_list = fox_followers['ids']

# and list of huffpo

huffpo_followers = t.followers.ids(screen_name='HuffingtonPost',count=2)
huffpo_list = huffpo_followers['ids']

# combine lists

full_user_list = fox_list + huffpo_list
	

# twitter ids of news handles	
	
news_ids = {	
	'USATODAY':	15754281,
	'MorningEdition':	20150502,
	'washingtonpost':	2467791,
	'CBSNews':	15012486,
	'nbcnightlynews':	8839632,
	'usnews':	6577642,
	'TIME':	14293310,
	'latimes':	16664681,
	'Cnnbrk':	428333,
	'todayshow':	7744592,
	'theearlyshow':	419117523,
	'NewsHour':	14437914,
	'abcworldnews':	2788713834,
	'Newsweek':	2884771,
	'gma':	22650211,
	'AC360': 227837742,
	'ajam':1178700896,
	'AJEnglish':4970411,
	'AlJazeera':76067316,
	'AlterNet':18851248,
	'BBC':19701628,
	'blackvoices':13557972,
	'BorowitzReport':17293897,
	'BuzzFeedBen':9532402,
	'chucktodd':50325797,
	'dailykos':20818801,
	'ezraklein':18622869,
	'GuardianUS':16042794,
	'HuffingtonPost':14511951,
	'HuffPostPol':15458694,
	'maddow':16129920,
	'mattyglesias':15446531,
	'MotherJones':18510860,
	'MoveOn':26657119,
	'msnbc':2836421,
	'NewsHour':14437914,
	'NewYorker':14677919,
	'NPR':14062180,
	'nprnews':5392522,
	'nprpolitics':5741722,
	'nytimes':807095,
	'PBS':12133382,
	'Salon':16955991,
	'Slate':15164565,
	'TheDailyShow':158414847,
	'thenation':1947301,
	'thinkprogress':55355654,
	'ACLJ':20791372,
	'AndrewBreitbart':18280993,
	'AnnCoulter':196168350,
	'SarahPalinUSA':65493023,
	'BreitbartNews':457984599,
	'cnsnews':34927577,
	'DRUDGE_REPORT':14669951,
	'DailyCaller':39308549,
	'FoxNews':1367531,
	'glennbeck':17454769,
	'HumanEvents':65146567,
	'instapundit':727472528,
	'michellemalkin':15976697,
	'oreillyfactor':23970102,
	'RealClearNews':20094138,
	'rushlimbaugh':342887079,
	'seanhannity':41634520,
	'theblaze':10774652,
	'townhallcom':28614262,
	'TuckerCarlson':22703645,
	'weeklystandard':17546958,
	'WSJ':3108351,
	'megynkelly':110445334,
	'michaeljohns':14828860,
	'Heritage':10168082,
	'RedState':3135241,
	'KarlRove':18791763,
	'newtgingrich':20713061,
	'fredthompson':2704951,
	'IngrahamAngle':50769180,
	'JoeNBC':21619519,
	'theMRC':20076659,
	'RonPaul':287413569,
	'JonahNRO':71627462,
	'NRO':19417492,
	'WashTimes':14662354,

	}

# see what other news handles users follow

users_news =[]

for user in full_user_list:

	id = user
	
	#user_info = t.users.lookup(user_id=id)
	#handle = user_info[0]['screen_name']

	friends = t.friends.ids(user_id=id)
	friend_list = friends['ids']

	#print friend_list
	user_news = []

	for key, value in news_ids.iteritems():
		if value in friend_list:
			user_news.append(key)
	
	users_news.append([id,user_news])	
	#time.sleep(60)

print users_news

df2 = pandas.DataFrame(users_news)
df2.columns = ['id', 'news follow']
df2.to_csv('users_news_5.csv')




