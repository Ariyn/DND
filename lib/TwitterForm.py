import lib.d40lib as d40lib, lib.TwitterEngine as TwitterEngine

class TwitterForm:
	def __init__(self, path = "../settings/twitterData.json"):
		print(path)
		self._path = path
		self.rtv = {}
		self.lib = d40lib.StdIOFile("settings/usermsg.json")
		self.lib.parseFile()
		self.infodata = []
		self.TMData = TwitterEngine.Twitter_Manager(path)
		# self.DND = TwitterEngine.DND_Twitter(path)

	def checkJson(self):
		if len(self.lib.jsonData) <= 0:
			self.lib.saveFile(self.lib.path,"","[]")
		else:
			self.infodata = self.lib.jsonReturn()

	def getRcvTwitInfo(self):
		self.message = self.TMData.receiveMessagePerID()
		# self.message = [{'created_at': 'Fri Jun 20 08:51:23 +0000 2014', 'text': '@ATLATCat01 naoekfloidasfadklsm', 'screen_name': 'YuiDevelop', 'id': '2560618506'}]
		# print(self.message)
		try:
			for j in range(len(self.message)):
				temp1 = ""
				temp2 = ""
				self.rtv = {}
				for i in self.message[j]:
					if i == "screen_name":
						temp1 = self.message[j][i]
					elif i == "text":
						temp2 = self.message[j][i]
						temp2 = temp2[temp2.find(" ")+1:]
				self.rtv[temp1] = temp2
				self.infodata.append(self.rtv)
				# self.lib.saveFile(self.lib.path,"",self.infodata)
				# self.checkJson()
		except:
			print("no data")
			return None

		return self.infodata

	def getUsers(self):
		return self.TMData.getUsers()
		
	def Send(self, userinfo):
		self.TMData.sendMessages(userinfo)