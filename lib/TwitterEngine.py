# -*- coding:utf-8 -*-

import codecs,sys
import json
import time
import threading
from twitter import Twitter, NoAuth, OAuth, read_token_file, TwitterHTTPError
from twitter.api import TwitterDictResponse, TwitterListResponse
# import twitter
# import twitter.api

def printu(text):
	sys.stdout.buffer.write((text+"\n").encode('utf-8'))


class DND_Twitter(object):
	accesses = []
	lastTwitter = None
	turn = 0

	def __init__(self, data):
		self.accesses = []
		for i in data['oauth']:
			oauth = OAuth(i[0][0], i[0][1], i[1][0], i[1][1])
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

	def sendMessageWithMedia(self, text, _media):
		self.accesses[self.turn].statuses.update_with_media(status = text, media = _media)
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
			if (self.lastTwitter['created_at'] == t['created_at']) and (self.lastTwitter['user']['id']  == t['user']['id']):
				if len(tempTwitter) > 0:
					self.lastTwitter = tempTwitter[0]
					return tempTwitter
				else:
					return tempTwitter
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

	def getUsers(self):
		return self.accesses[self.turn].followers.ids()

	def getShow(self, ID):
		return self.accesses[self.turn].users.show(user_id = ID)


class Twitter_Manager(object):
	twitters = []
	masterTwitter = None
	sender = 0

	def __init__(self, path):
		self.path = path
		self.file = codecs.open(self.path, 'r', 'utf8')
		self.twitterData = {}
		ouathData = {}
		ouathText = ""
		for line in self.file:
			ouathText += line
		self.twitterData = json.loads(s = ouathText)
		i = 0
		while i != len(self.twitterData):
			data = self.twitterData[i]
			if i == 0:
				self.masterTwitter = DND_Twitter(data)
			else:
				self.twitters.append(DND_Twitter(data))
			i+=1

	def sendMessage(self, text):
		try:
			if(len(text) > 140):
				i = 0
				while i != (len(text) / 140) + 1:
					s = text[i * 140 + 1:140*(i+1)]
					self.twitters[self.sender].sendMessage(s)
					i+=1
			else:
				self.twitters[self.sender].sendMessage(text)
		except TwitterHTTPError as e:
			print("twitter" + str(self.sender) + " is error : " + str(e))
			if(len(self.twitters) - 1 == self.sender):
				self.sender = 0
			else:
				self.sender += 1
			self.sendMessage(text)

	def sendMessageWithScreen_name(self, text, screen_name):
		message = "@" + screen_name + " " + text
		self.sendMessage(message)

	def sendMessageWithMedia(self, text, _media):
		if(len(text) > 140):
			print("message is over 140 characters")
			return False
		try:
			self.twitters[self.sender].sendMessageWithMedia(text, _media)
		except TwitterHTTPError as e:
			print("twitter" + str(self.sender) + " is error : " + str(e))
			if(len(self.twitters) - 1 == self.sender):
				self.sender = 0
			else:
				self.sender += 1

	def sendMessageForMasterTwitter(self, text):
		if(len(text) > 140):
			print("message is over 140 characters")
			return False
		try:
			self.masterTwitter.sendMessage(text)
		except TwitterHTTPError as e:
			print("masterTwitter is error : " + str(e))
			return False

	def saveLastTwitter(self):
		for i, t in enumerate(self.twitterData):
			if i == 0:
				t['lastTwitter'] = self.masterTwitter.lastTwitter
			else:
				t['lastTwitter'] = self.twitters[i-1].lastTwitter

		f = codecs.open(self.path, 'w', 'utf8')
		json.dump(self.twitterData, f)

	def receiveMessage(self):
		message = []
		try:
			for t in self.twitters:
				message.append(t.getTimeline())
			self.saveLastTwitter()
		except TwitterHTTPError as e:
			print("receiveMessage is False :" + str(e))
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
					_id['id'] = m['user']['id_str']
					_id['screen_name'] = m['user']['screen_name']
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
		except TwitterHTTPError as e:
			print("receiveMessage is False :" + str(e))
			return False
		return ids

	def getUsers(self):
		return self.masterTwitter.getUsers()

	def getScreenName(self, ID):
		return self.masterTwitter.getShow(ID)["screen_name"]

	def sendMessages(self, messages):
		for message in messages:
			ID = message['id']
			text = message['text']
			thread = threading.Thread(target = self.sendMessageWithScreen_name, args = (text, ID))
			thread.start()