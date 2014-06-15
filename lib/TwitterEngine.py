# -*- coding:utf-8 -*-

import codecs,sys
import json
import time
from twitter import Twitter, NoAuth, OAuth, read_token_file, TwitterHTTPError
from twitter.api import TwitterDictResponse, TwitterListResponse

def printu(text):
	sys.stdout.buffer.write((text+"\n").encode('utf-8'))


class DND_Twitter(object):
	accesses = []
	lastTwitter = None
	turn = 0

	def __init__(self, data):
		self.accesses = []
		for i in data['oauth']:
			#print(i)
			print(i[0][0]+"\n", "'"+i[0][1]+"\n", "'"+i[1][0]+"\n", "'"+i[1][1]+"\n")
			oauth = OAuth(token = i[0][0], token_secret = i[0][1], consumer_key = i[1][0], consumer_secret = i[1][1])
			twitter = Twitter(domain='api.twitter.com',
                  					auth=oauth,
                    				api_version='1.1')
			self.accesses.append(twitter)
		self.lastTwitter = data['lastTwitter']

	def sendMessage(self, text):
		self.accesses[self.turn].statuses.update(status = text)
		if(self.turn == len(self.accesses)-1):
			self.turn = 0
		else:
			self.turn += 1
		
	def getTimeline(self):
		newTwitter = self.accesses[self.turn].statuses.mentions_timeline()
		if(self.turn == len(self.accesses)-1):
			self.turn = 0
		else:
			self.turn += 1

		if(self.lastTwitter == None):
			self.lastTwitter = newTwitter[len(newTwitter)-1]

		tempTwitter = []
		for t in newTwitter:
			if (self.lastTwitter['created_at'] == t['created_at']) and (self.lastTwitter['user']['screen_name']  == t['user']['screen_name']):
				if len(tempTwitter) > 0:
					self.lastTwitter = tempTwitter[len(tempTwitter)-1]
			else:
				tempTwitter.append(t)
		return tempTwitter
		
	def getLimit(self):
		limits = []
		i = 0
		while i != len(accesses)-1 :
			limits.append[self.accesses[i].application.rate_limit_status()]
			i += 1
		return limits


class Twitter_Manager(object):
	twitters = []
	sender = 0

	def __init__(self, path = '.'):
		self.file = codecs.open(path, 'r', 'utf8')
		self.twitterData = {}
		ouathData = {}
		ouathText = ""
		for line in self.file:
			ouathText += line
		self.twitterData = json.loads(s = ouathText)
		i = 0
		while i != len(self.twitterData):
			data = self.twitterData[i]
			self.twitters.append(DND_Twitter(data))
			i+=1

	def sendMessage(self, text):
		if(len(text) > 140):
			print("message is over 140 characters")
			return False
		try:
			self.twitters[self.sender].sendMessage(text)
		except TwitterHTTPError as e:
			print("twitter" + str(self.sender) + " is error : " + str(e))
			if(len(self.twitters) - 1 == self.sender):
				self.sender = 0
			else:
				self.sender += 1
			self.sendMessage(text)

	def sendMessageWithID(self, text, screen_name):
		message = "@" + screen_name + " " + text
		self.sendMessage(text)

	def saveLastTwitter(self):
		for i, t in enumerate(self.twitterData):
			t['lastTwitter'] = self.twitters[i].lastTwitter

		f = codecs.open("Oauth.json", 'w', 'utf8')
		json.dump(self.twitterData, f)

	def receiveMessage(self):
		message = []
		try:
			for t in self.twitters:
				message.append(t.getTimeline())
			self.saveLastTwitter()
		except:
			return False
		return message

	def receiveLimit(self):
		message = []
		for t in self.twitters:
			message.append(t.getLimit())
		return message

	def receiveMessagePerID(self):
		ids = []
		try:
			for t in self.twitters:
				message = t.getTimeline()
				_id = {}
				for m in message:
					_id['id'] = m['user']['screen_name']
					_id['text'] = m['text']
					_id['created_at'] = m['created_at']
					flag = False
					for i in ids:
						if i['id'] == _id['id']:
							flag = True
					if flag == True:
						continue
					else:
						ids.append(_id)

			self.saveLastTwitter()
		except:
			return False
		return ids

if __name__ == "__main__":
	tw = Twitter_Manager(path = "Oauth.json")

	tw.sendMessage("Twitter Test. Does this will work well??")
