# -*- coding:utf-8 -*-

import sys, codecs, json
from os import listdir, path

def print(*text):
	sys.stdout.buffer.write((str(text)+"\n").encode('utf-8'))

class DndError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

# class dict(dict):
# 	pass

class dndMysqlClass:
	DataTable = {}
	def __init__(self):
		comp, reason = self.checkJsonDatas()
		
		if not comp:
			self.failed = True
			raise DndError(reason)
		else:
			self.__initCategoryTable__()

	def __initCategoryTable__(self):
		#self.CategoryTable = {"ariyn":["hp"]}
		#self.DataTable = {"ariyn":{"hp":30},"engine":{}}
		pass

	def checkJsonDatas(self):
		fileLists = listdir(path.abspath("../settings/"))
		if "settings.json" not in fileLists:
			return False, "No \"settings.json\""
		else:
			try:
				_string = codecs.open(path.abspath("../settings/settings.json"), "r", "utf-8")
				string = _string.read()
				_string.close()

			except FileNotFoundError as err:
				#return False, err
				raise DndError(err)

			try:
				string = json.loads(string)
				#self.CategoryTable = [x[:-5] for x in string]
			except ValueError as err:
				#print(err)
				#return False, err
				raise DndError(err)

			for i in string:
				if i not in fileLists:
					return False, "No \""+i+"\" in settings folder"

			for i in [x for x in fileLists if x in string]:
				print(i)
				data = codecs.open(path.abspath("../settings/"+i),"r","utf-8")
				data = data.read()
				try:
					data = json.loads(data)
				except ValueError as err:
					#return False, err
					raise DndError(err)

				try:
					self.DataTable[i[:-5]] = data
				except AttributeError as err:
					#return False, err
					raise DndError(err)
				
			self.fileLists = fileLists
			return True, ""

	def setData(self, category, key, value):
		if (category in self.DataTable) and (key in self.DataTable[category]):
			self.DataTable[category][key] = value

	def appendData(self, category, key, value):
		if (category in self.DataTable) and (key in self.DataTable[category]):
			self.DataTable[category][key] += value

	def getData(self, category, key = None):
		if category in self.DataTable:
			if key == None:
				return self.DataTable[category]
			elif self.getDataKey(category, key):
				return self.DataTable[category][key]
	
	def save(self):
		for i in self.fileLists:
			files = codecs.open(path.abspath("../settings/"+i),"w", "utf-8")
			data = self.getData(character)
			try:
				data = json.dumps(data)
			except ValueError as err:
				raise DndError(err)

			files.write(data)
			files.close()

	def getDataKey(self, category, key):
		keys = key.split(".")
		print(self.DataTable)
		if category in self.DataTable:
			header = self.DataTable[category]

			for i in keys:
				if i in header:
					header = header[i]
				else:
					raise DndError("No such Data like "+".".join(keys[keys.index(i):]))
		#pass

if __name__ == "__main__":
	d = dndMysqlClass()
	print(d.getDataKey("characters", "miko"))
	#d.setData("ariyn", "hp", 30)
