import pdb
import codecs
import sys, json, re

def printu(text):
	sys.stdout.buffer.write((text+"\n").encode('utf-8'))

class StdIOFile:
	def __init__(self,  path = ""):
		self.path = path
		self.jsonText = ""
		self.file = codecs.open(self.path,'r',"utf8")

	def readFile(self):
		for lines in self.file:
			self.jsonText += lines

	def parseFile(self):
		self.readFile()
		self.jsonData = json.loads(s=self.jsonText)

	def jsonReturn(self):
		self.parseFile()
		return self.jsonData

	def JsonToTranslate(self, string):
		return str(string).replace("'", "\"")
		