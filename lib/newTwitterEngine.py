# -*- coding:utf-8 -*-

import codecs, sys, os
import json, time
import concurrent.futures
from twitter import Twitter, NoAuth, OAuth, read_token_file, TwitterHTTPError
from twitter.api import TwitterDictResponse, TwitterListResponse
import twitter as originalTwitter
# import twitter.api

class DND_Twitter(object):
	accesses = {}
	consumer_key, consumer_serect = [],[]
	bots, followers = {}, []
	
	def __init__(self, path):
		files = codecs.open(path,"r","utf-8")
		fileData = files.read()
		jsonData = json.loads(fileData)

		if "oauth" in jsonData:
			self.consumer_key = jsonData["oauth"]["consumer_key"]
			self.consumer_serect = jsonData["oauth"]["consumer_serect"]

		for i in jsonData:
			if i != "oauth":
				print(i)
				self.bots[i], e = jsonData[i], jsonData[i]
				self.bots[i]["last_twit_id"] = ""

				acc = []
				for ck, cs, at, ats in zip(self.consumer_key, self.consumer_serect,e["access_token"],e["access_token_serect"]):
					#print(i +"= "+e["id_number"]+"-"+at)
					oauth = OAuth(e["id_number"]+"-"+at, ats,
									ck, cs)
					twitter = Twitter(domain='api.twitter.com',auth=oauth,api_version='1.1')
					#print(twitter)
					acc.append(twitter)
					time.sleep(0.05)

				self.accesses[i] = acc

		self.fileData, self.jsonData = fileData, jsonData

	def getLimits(self):
		limits, jsonLimits = {}, {}
		for i in self.accesses:
			for e in self.accesses[i]:
				#print(e)
				data = e.application.rate_limit_status()
				limits[i], jsonLimits[i] = [], []
				limits[i].append(data)
				#jsonLimits[i].append(json.loads(data))

		self.jsonLimits, self.limits = jsonLimits,limits
		return limits

	def getUsers(self):
		data = self.accesses["DNDMATSER"][0].followers.ids()
		self.accesses["DNDMATSER"][0].users.lookup(user_id = data["ids"])

	def getTimeLines(self, row = False):
		twit = []
		for i in self.accesses:
			twit.append(self.getTimeLine(i, row))

	def getTimeline(self, id, row = False):
		#newTwitter = []
		#for i in self.accesses:
		twit = self.accesses[id][self._getSenderBot(id)].statuses.mentions_timeline()
		
		timeList = [x["id_str"] for x in twit if x["id_str"] == self.bots[id]["last_twit_id"]]
		if len(timeList):
			print([x["id_str"] for x in twit].index(timeList[0]))
			twit = twit[:[x["id_str"] for x in twit].index(timeList[0])]
			self.bots[id]["last_twit_id"] = timeList[0]
		
		self.bots[id]["newtwit"] = twit

		if not row:
			retTwit = [
				{x["user"]["screen_name"]:x["text"]} for x in twit
			]
		else:
			retTwit = twit
		return retTwit

	def sendMessages(self, messages):
		self.th = []
		excutor = concurrent.futures.ThreadPoolExecutor(max_workers=len(messages))
		for message in messages:
			ID = message['id']
			text = message['text']

			if "media" in message:
				media = message["media"]
				if not os.path.exists(media):
					media = None
				else:
					#print("encoding")
					media = open(media,"rb").read()
					#print(media)
			else:
				media = None

			sender = self._getSenderBot()
			access = self.accesses[sender][self._getSenderBot(sender)]

			#test = access.statuses.update_with_media(**{"status" : text, "media[]": media})
			#print(test)
			thread = excutor.submit(self._sendMessageThread, access, sender, text, ID, media, self.th)

	def _getSenderBot(self, name = None):
		if name == None:
			return "DNDMATSER"
		else:
			return 2
		pass

	@staticmethod
	def _sendMessageThread(access, sender, text, screen_name, media,th):
		text = "@" + screen_name + " " + text
		if media:
			update = access.statuses.update_with_media
		else:
			update = access.statuses.update
		try:
			if(len(text) > 140):
				i = 0
				while i != (len(text) / 140) + 1:
					s = text[i * 140 + 1:140*(i+1)]
					if media:
						update(**{"status" : s, "media[]": media})
					else:
						update(status = s)
					i+=1
			else:
				if media:
					ass = access.statuses.update_with_media(**{"status":text, "media[]": media})

				else:
					update(**{"status" : text})
		except TwitterHTTPError as e:
			print("twitter " + str(sender) + " is error : " + str(e))

		th.append(True)

	@staticmethod
	def _parseTimeData(data):
		return time.mktime(time.strptime(data, "%a %b %d %H:%M:%S +0000 %Y"))

if __name__ == "__main__":
	d = DND_Twitter("../settings/oauth.json")
	#print(originalTwitter.__file__)
	#print(originalTwitter.api.__file__)
	print(d.accesses)
	#print(d.accesses["DNDMATSER"][0].application.rate_limit_status())
	#print(d.getLimits())
	print(d.getUsers())
	#print(d.getUsers())
	#d.sendMessages([{"id":"Mutopia_ArtTeam","text":"sexy picture 4 for my soul","media":os.path.abspath("../DND/resource/test2.gif")}])
	# d.sendMessages([
	# 	{"id":"Mutopia_ArtTeam","text":"sexy string for my soul"},
	# 	{"id":"DNDBOT1","text":"sexy string for my soul"},
	# 	{"id":"DNDBOT2","text":"sexy string for my soul"},
	# 	{"id":"DNDBOT3","text":"sexy string for my soul"}
	# 	])

	# print(d.th, len(d.th))

	#sys.stdout.buffer.write(str(d.getTimeline("DNDMATSER")).encode("utf-8"))
