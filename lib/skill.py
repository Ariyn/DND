import d40lib, json, sys, codecs
import dice

class Skills:
	attr = None
	def __init__(self, path = "../settings/skills.json"):
		self._path = path
		self.lib = d40lib.StdIOFile(path)
		self.jsonData = self.lib.jsonReturn()
		self.name = {}
		self.rtName = []
		self.getAllObject()

		# try:
		# 	self.file = codecs.open(path,"r","utf-8")
		# except FileNotFoundError as err:
		# 	print(err)
		# 	return None

	def getAllObject(self):
		self.name = self.jsonData

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

	def setObjtoName(self, obj, attribute = "", val1 = None):
		self.innerSetObj(obj, attribute, val1)
		# self.name[] = obj
		# self.addUser()
		
	def addUsers(self):
		for key in self.name:
			self.rtName.append(self.name[key])

	def saveFile(self, path = "", name = ""):
		self.addUsers()
		self.lib.saveFile(path, name, self.name)

	def printAllObject(self):
		for key in self.name.keys():
			print(key, self.name[key])

# 		self.jsonData = self.file.read()
# 		try:
# 			self.data = json.loads(self.jsonData)
# 		except ValueError as err:
# 			print(err)
# 			return None

# 	def appendChar(self, data):
# 		self.character = data

# 	def parseData(self, character, data):
# 		spliText = data.split(" ")
# 		pass

# 	def getData(self, name):
# 		if name in [x["name"] for x in self.data]:
# 			ind = [x["name"] for x in self.data].index(name)
# 			return self.data[ind]
# 		else:
# 			return None

# def main():
# 	s = skill()
# 	sys.stdout.buffer.write(str(s.getData("파이어볼")).encode("utf-8"))

if __name__ == "__main__":
	a = Skills()
	# a.setObjtoName(a.getNameis("heal"), "damage", -5)
	# a.saveFile(a._path,"")
	print(a.getObjtoName(a.getNameis("heal"), "damage"))
	a.printAllObject()