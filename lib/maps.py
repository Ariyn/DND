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

	def __init__(self, string = "5x5", floor = 1):
		if string == "5x5":
			self.Size = 5
			self.prob = 40
		elif string == "3x3":
			self.Size = 3
			self.prob = 30
		else:
			pass
		self.jsonData = []
		self.index = -1
		self.mapname = ""
		self.roomdata = "["
		self.floor = floor
		self.completeMaps()

	def completeMaps(self):
		for i in range(self.floor):
			self.createMaps()
			self.setNumber(i+1)
			self.jsonData.append(self.roomdata)
			self.ToJson("D",i)
			self.roomdata = "["
			self.fstStep = True


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
					# if(self.fstStep is False):
					# 	pass
						# self.index += 1
						# self.MapTable[i][j].Number = self.index
					# west per 1 point cell check
					# 
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
						# if(self.MapTable[i][j].ConCT == 0):
						# 	pass
						# else:
						# 	self.setRoomInfo(self.index, self.MapTable[i][j].Value, floor)
						# 	if(i is self.Size - 1 and j is self.Size - 1):
						# 		pass
						# 	else:
						# 		self.roomdata += ","
						pass

			if(self.fstStep):
				self.fstStep = False
			else:
				break
		# self.roomdata += "]"
		# self.roomdata = self.roomdata.replace(",]","]")
		# empty map delete
		self.prevent()

	def setNumber(self, floor):
		tmpindex = -1
		# print(self.Size)
		for i in range(self.Size):
			for j in range(self.Size):
				try:
					tmpindex += 1
					# print(tmpindex)
					self.MapTable[i][j].Number = tmpindex
					self.setRoomInfo(self.MapTable[i][j].Number, self.MapTable[i][j].Value, floor)
					if(i is self.Size - 1 and j is self.Size - 1):
						pass
					else:
						self.roomdata += ","
				except:
					tmpindex -= 1
		self.roomdata += "]"
		self.roomdata = self.roomdata.replace(",]","]")

	def findNumber(self, number):
		for i in range(self.Size):
			for j in range(self.Size):
				try:
					if(self.MapTable[i][j].Number == number):
						return self.MapTable[i][j].returnJson()
				except:
					print("number: ", index," Empty.")

	def setMapList(self):
		self.MapTable = []
		for x in range(self.Size):
			self.MapTable.append([]*self.Size)
		# create object in MapList
		for i in range(self.Size):
			for j in range(self.Size):
				self.MapTable[i].append(mapinfo.D40Map())

	def printMaptable(self):
		for i in self.jsonData:
			print(i)

	def ToJson(self, name = "", number = 1):
		self.file = codecs.open("../settings/map-"+ name + str(number) +".json", 'w', 'utf-8')
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

	def setRoomInfo(self, number, con = [None], floor = 0):
		self.roomdata += "{"
		self.roomdata += "\"number\":"+ str(number).replace("'","\"").replace("None","null") +","
		self.roomdata += "\"floor\":["+ str(floor).replace("'","") +"],"
		self.roomdata += "\"connections\":" + str(con).replace("'","\"").replace("None","null") +"}"
		# self.roomdata += "\"objects\":" + str(objects).replace("'","\"").replace("None","null") + "}"


# sample code
if __name__ == "__main__":
	a = Maps("3x3", 2)
	# c = a.spcMapSelect(5)
	# a.printMaptable()

	# print(c)
	# a.printMaptable()
	# print(randrange(0,5))
	# print(a.MapTable[0][0].Value)