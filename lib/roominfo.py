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
	def __init__(self, path = "../settings/roominfo.json"):
		self.lib = d40lib.StdIOFile(path)
		self.jsonData = self.lib.jsonReturn()
		self.number = {}
		self.getAllObject()

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
			tmpnumber = i['number']
			self.number[tmpnumber] = i

		# self.number = self.jsonData['number']
		# self.name = self.jsonData['name']
		# self.items = self.jsonData['items']
		# self.events = self.jsonData['events']
		# self.monsters = self.jsonData['monsters']

	# # number
	# def getNumber(self):
	# 	return self.number
	# def setNumber(self, val):
	# 	self.number = val
	# # name
	# def getName(self):
	# 	return self.name
	# def setName(self, string):
	# 	self.name = string
	# # items -> type : list in python , but array type in json
	# def getItems(self):
	# 	return self.items
	# def setItems(self, lists):
	# 	self.items = lists
	# def addItem(self, val):
	# 	self.items.append(val)
	# def delItem(self, val):
	# 	if self.items.number(val) is not None:
	# 		self.items.remove(val)
	# 	else:
	# 		print(val," is not exist")
	# # events -> type : dict in python, but object type in json
	# def getEvents(self):
	# 	return self.events
	# def setEvents(self, dicts):
	# 	self.events = dicts
	# def addEvent(self, key, val):
	# 	if(type(key) is int):
	# 		if(type(val) is int ):
	# 			vallist = [str(val), "%"]
	# 			self.events[str(key)] = ''.join(vallist)
	# def delEvent(self, key):
	# 	if(type(key) is int):
	# 		if(str(key) in self.events):
	# 			del self.events[str(key)]
	# 		else:
	# 			print(key, " is not exist")
	# 	else:
	# 		del self.events[key]
	# # monsters -> type : list in python, but array type in json
	# def getMonsters(self):
	# 	return self.monsters
	# def setMonsters(self, lists):
	# 	self.monsters = lists
	# def addMonster(self, val):
	# 	self.monsters.append(val)
	# def delMonster(self, val):
	# 	if self.monsters.number(val) is not None:
	# 		self.monsters.remove(val)
	# 	else:
	# 		print(val, " is not exist")



	# debug functions
	def printAllObject(self):
		for key in self.number.keys():
			print(key, self.number[key])
		# print("number	: ", self.number)
		# print("name 	: ", self.name)
		# print("items 	: ", self.items)
		# print("events 	: ", self.events)
		# print("monsters	: ", self.monsters)




if __name__ == "__main__":
	a = Rooms()
	a.printAllObject()