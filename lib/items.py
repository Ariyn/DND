import d40lib
import pdb
import codecs
import sys, json, re

def printu(text):
	sys.stdout.buffer.write((text+"\n").encode('utf-8'))

class Items:
	def __init__(self, path = "../settings/items.json"):
		self.lib = d40lib.StdIOFile(path)
		self.jsonData = self.lib.jsonReturn()
		self.name = {}
		self.getAllObject()

	def getAllObject(self):
		for i in self.jsonData:
			tmpname = i['name']
			self.name[tmpname] = i

	def printAllObject(self):
		for key in self.name.keys():
			print(key, self.name[key])

	def ToJson(self):
		return self.jsonData

if __name__ == "__main__":
	a = Items()
	a.printAllObject()