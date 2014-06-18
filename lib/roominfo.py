# how to use
# use in automatically
# first import roominfo, json, sys, re, codecs
# second make functions
# def printu(text):
# 	sys.stdout.buffer.write((text+"\n").encode('utf-8'))
# open your room json file, so you define value.
# sample code
# import roominfo
# import json
# import codecs
# import sys, re


# def printu(text):
# 	sys.stdout.buffer.write((text+"\n").encode('utf-8'))

# if __name__ == "__main__":
# 	room = roominfo.SetRoom("./roominfo.json", "no")
# 	room.setAuto()
# 	room.printAllObject()
# example output result
# number	:  0
# name 	:  name
# items 	:  ['item1']
# events 	:  {'23': '30%', '27': '40%', '0': '30%'}
# monsters	:  ['monster1']
# [Finished in 0.1s]
import json
import codecs
import mapinfo
import d40lib
import sys, re

def printu(text):
	sys.stdout.buffer.write((text+"\n").encode('utf-8'))

class Rooms:
	attr = None
	def __init__(self, path = "../settings/roominfo.json"):
		self._path = path
		self.lib = d40lib.StdIOFile(path)
		self.jsonData = self.lib.jsonReturn()
		self.name = {}
		self.rtName = []
		self.getAllObject()
		self.ToJson()

	# getter, setter
	# def setAllObject(self, valnumber, valname, valitems, valevents, valmonsters):
	# 	self.setNumber(valnumber)
	# 	self.setName(valname)
	# 	self.setItems(valitems)
	# 	self.setEvents(valevents)
	# 	self.setMonsters(valmonsters)

	# def setAuto(self):
		# self.setNumber(self.number)
		# self.setName(self.name)
		# self.setItems(self.items)
		# self.setEvents(self.events)
		# self.setMonsters(self.monsters)

	def getAllObject(self):
		for i in self.jsonData:
			tmpnumber = i['name']
			self.name[tmpnumber] = i

	def getNameis(self, name = None):
		try:
			for key in self.name.keys():
				if key == name:
					return self.name[key]
		except:
			return None

	def getObjtoName(self, obj, attribute = ""):
		if attribute in obj:
			# print(obj)
			self.attr = obj[attribute]
		else:
			for key in obj.keys():
				if((type(obj[key]) is dict)):
					if attribute in obj[key]:
						self.attr = self.getObjtoName(obj[key], attribute)
				if(type(obj[key]) is list):
					try:
						for i in obj[key]:
							self.attr = self.getObjtoName(i, attribute)
					except:
						pass
					for i in obj[key]:
						if(i == attribute):
							self.attr = i

		return self.attr


	def innerSetObj(self, obj, attribute = "", val1 = 0):
		try:
			for key in obj.keys():
				if(key == attribute):
					obj[key] = val1
				elif((type(obj[key]) is dict) or (type(obj[key]) is list)):
					self.innerSetObj(obj[key], attribute, val1)
					pass
		except:
			return None

	def ToJson(self):
		self.rtName = []
		for i in self.name.keys():
			self.rtName.append(self.name[i])

	def setObjtoName(self, obj, attribute = "", val1 = 0):
		self.innerSetObj(obj, attribute, val1)
		self.ToJson()

	# debug functions
	def printAllObject(self):
		for key in self.name.keys():
			print(key, self.name[key])

	def saveFile(self, path = "", name = "", string = ""):
		self.lib.saveFile(path, name, string)

if __name__ == "__main__":
	a = Rooms()
	print(a.getNameis("room-2"))
	# a.setObjtoName(a.getNameis("room-2"), "")
	print(a.getObjtoName(a.getNameis("room-2"), "monster1"))