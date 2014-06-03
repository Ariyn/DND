# how to use
# first import maps, json, codecs, sys, re
# second define value.
# sample code
# import maps
# import json
# import codecs
# import sys, re

# if __name__ == "__main__":
# 	rmap = maps.Maps()
# 	rmap.createMaps()
# 	rmap.printRoomInfo()

import json
import codecs
import mapinfo
import sys, re
from random import choice, randrange

class Maps:
	cons = ["North", "South", "West", "East", "Up", "Down"]

	def __init__(self, string = "5x5"):
		if string == "5x5":
			self.Size = 5
			self.prob = 40
		elif string == "3x3":
			self.Size = 3
			self.prob = 30
		else:
			pass
		self.index = -1
		self.mapname = ""
		self.roomdata = "["
		self.createMaps()

	# temp function for prototype
	def createMaps(self):
		# if 5 by 5 size then -
		self.fstStep = True
		self.setMapList()
		# set value
		#set communication each others
		while(True):
			for i in range(self.Size):
				for j in range(self.Size):
					# room index
					if(self.fstStep is False):
						self.index += 1
						self.MapTable[i][j].Index = self.index
					# west per 1 point cell check
					if(j-1>=0):
						if(self.MapTable[i][j-1].East):
							self.MapTable[i][j]._callWest()
						else:
							if(randrange(0,100)<self.prob and self.fstStep):
								self.MapTable[i][j]._callWest()
								# rand % create west connection

					if(j+1<self.Size):
						if(self.MapTable[i][j+1].West):
							self.MapTable[i][j]._callEast()
						else:
							if(randrange(0,100)<self.prob and self.fstStep):
								self.MapTable[i][j]._callEast()
								# rand % create East connection

					if(i-1>=0):
						if(self.MapTable[i-1][j].South):
							self.MapTable[i][j]._callNorth()
						else:
							if(randrange(0,100)<self.prob and self.fstStep):
								self.MapTable[i][j]._callNorth()
								# rand % create North connection

					if(i+1<self.Size):
						if(self.MapTable[i+1][j].North):
							self.MapTable[i][j]._callSouth()
						else:
							if(randrange(0,100)<self.prob and self.fstStep):
								self.MapTable[i][j]._callSouth()
								# rand % create South connection

					if(self.index == (self.Size*self.Size)-1):
						self.MapTable[i][j]._callDown()

					if(self.fstStep):
						pass
					else:
						# self.setRoomInfo(self.index, self.MapTable[i][j].Value, self.MapTable[i][j].Events, self.MapTable[i][j].Objects)
						if(self.MapTable[i][j].ConCT == 0):
							pass
						else:
							self.setRoomInfo(self.index, self.MapTable[i][j].Value)
							if(i is self.Size - 1 and j is self.Size - 1):
								pass
							else:
								self.roomdata += ","
			if(self.fstStep):
				self.fstStep = False
			else:
				break
		self.roomdata += "]"
		self.roomdata = self.roomdata.replace(",]","]")
		# empty map delete
		self.prevent()

	def spcMapSelect(self, index):
		for i in range(self.Size):
			for j in range(self.Size):
				try:
					if(self.MapTable[i][j].Index == index):
						return self.MapTable[i][j].returnJson()
				except:
					print("index: ", index," Empty.")

	def setMapList(self):
		self.MapTable = []
		for x in range(self.Size):
			self.MapTable.append([]*self.Size)
		# create object in MapList
		for i in range(self.Size):
			for j in range(self.Size):
				self.MapTable[i].append(mapinfo.D40Map())

	def printMaptable(self):
		print(self.roomdata)

	def ToJson(self):
		self.file = codecs.open("./map.json", 'w', 'utf-8')
		for i in self.roomdata:
			self.file.write(i)

	def isNoneMap(self, val1, val2):
		if self.MapTable[val1][val2] is None:
			return True

	def prevent(self):
		for i in range(self.Size):
			for j in range(self.Size):
				if(self.MapTable[i][j].ConCT == 0):
					del self.MapTable[i][j].Value


# attention json data (espacially in list)
# adding array symbol '[', and appending middle symbol ','
	# def setRoomInfo(self, number, con = [None], events = {None}, objects = {None}):
	# 	self.roomdata += "{"
	# 	self.roomdata += "\"index\":"+ str(number).replace("'","\"").replace("None","null") +","
	# 	self.roomdata += "\"events\":[" + str(events).replace("'","\"").replace("None","null") +"],"
	# 	self.roomdata += "\"connections\":" + str(con).replace("'","\"").replace("None","null") +","
	# 	self.roomdata += "\"objects\":" + str(objects).replace("'","\"").replace("None","null") + "}"

	def setRoomInfo(self, number, con = [None], floor = ""):
		self.roomdata += "{"
		self.roomdata += "\"number\":"+ str(number).replace("'","\"").replace("None","null") +","
		self.roomdata += "\"floor\":["+ floor +"],"
		self.roomdata += "\"connections\":" + str(con).replace("'","\"").replace("None","null") +"}"
		# self.roomdata += "\"objects\":" + str(objects).replace("'","\"").replace("None","null") + "}"


# sample code
if __name__ == "__main__":
	a = Maps("3x3")
	b = a.ToJson()
	c = a.spcMapSelect(5)
	a.printMaptable()
	print(c)

	# print(c)
	# a.printMaptable()
	# print(randrange(0,5))
	# print(a.MapTable[0][0].Value)