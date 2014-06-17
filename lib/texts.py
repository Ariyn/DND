import d40lib
import pdb
import codecs
import sys, json, re

class Texts:
	def __init__(self, path = "../settings/texts.json"):
		self._path = path
		self.lib = d40lib.StdIOFile(path)
		self.jsonData = self.lib.jsonReturn()
		self.name = {}
		self.rtName = []
		#self.getAllObject()
		self.ToJson()


	def getNameis(self, name = None):
		try:
			for key in self.name.keys():
				if key == name:
					return self.name[key]
		except:
			return None

	def getObjtoName(self, obj, attribute = ""):
		try:
			for key in obj.keys():
				if(key == attribute):
					return obj[key]
				elif(type(obj[key]) is dict):
					return attribute, obj[key][attribute]
					pass
				elif(type(obj[key]) is list):
					self.getObjtoName(obj[key], attribute)
		except:
			return None

	def setObjtoName(self, obj, attribute = "", val1 = 0):
		self.innerSetObj(obj, attribute, val1)
		self.ToJson()

	def innerSetObj(self, obj, attribute = "", val1 = 0):
		try:
			for key in obj.keys():
				if(key == attribute):
					obj[key] = val1
				elif((type(obj[key]) is dict) or (type(obj[key]) is list)):
					self.innerSetObj(obj[key], attribute)
		except:
			return None

	def printAllObject(self):
		for key in self.name.keys():
			print(key, self.name[key])

	def ToJson(self):
		self.rtName = []
		for i in self.name.keys():
			self.rtName.append(self.name[i])

	def saveFile(self, path = "", name = "", string = ""):
		self.lib.saveFile(path, name, string)
