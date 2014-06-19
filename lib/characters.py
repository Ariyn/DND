import d40lib
import pdb
import codecs
import sys, json, re

def printu(text):
	sys.stdout.buffer.write((text+"\n").encode('utf-8'))

class Character:
	attr = None
	def __init__(self, path = "../settings/characters.json"):
		self._path = path
		self.lib = d40lib.StdIOFile(path)
		self.jsonData = self.lib.jsonReturn()
		self.name = {}
		self.rtName = []
		self.getAllObject()
		self.ToJson()

	def getAllObject(self):
		for i in self.jsonData:
			tmpname = i['charname']
			self.name[tmpname] = i
			
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
					for i in obj[key]:
						self.attr = self.getObjtoName(i, attribute)

		return self.attr

		# retVal = None
		# 	# print(obj)
		# for key in obj.keys():
		# 	# print(key)
		# 	# print(key+ ":"+ attribute + "\t" +str(type(obj[key])))
		# 	if(key == attribute):
		# 		retVal = obj[key]
		# 	elif(type(obj[key]) is dict):
		# 		retVal = self.getObjtoName(obj[key], attribute)
		# 	elif(type(obj[key]) is list):
		# 		for i in obj[key]:
		# 			retVal = self.getObjtoName(i, attribute)
		# return retVal

	def setObjtoName(self, obj, attribute = "", val1 = 0, ptype= None):
		self.innerSetObj(obj, attribute, val1, ptype)
		self.ToJson()
		

<<<<<<< HEAD
	def innerSetObj(self, obj, attribute = "", val1 = 0):
		# if attribute in obj:
		# 	# print("seu")
		# 	obj[attribute] = val1
		# else:
		# 	for key in obj.keys():
		# 		if((type(obj[key]) is dict)):
		# 			if attribute in obj[key]:
		# 				self.innerSetObj(obj[key], attribute)
		# 		if(type(obj[key]) is list):
		# 			for i in obj[key]:
		# 				self.innerSetObj(i, attribute)
		# ------------------------------------------------------
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

	def printAllObject(self):
		for key in self.name.keys():
			print(key, self.name[key])

	def saveFile(self, path = "", name = "", string = ""):
		self.lib.saveFile(path, name, string)
		
if __name__ == "__main__":
	a = Character("../settings/characters.json")
	# print(a.getNameis("horo"))
	# print(a.getObjtoName("horo", "status"))
	print(a.getObjtoName(a.getObjtoName(a.getNameis("horo"), "status"), "hp"))



