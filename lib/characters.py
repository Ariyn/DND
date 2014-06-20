import d40lib
import pdb
import codecs
import sys, json, re

def printu(text):
	sys.stdout.buffer.write((text+"\n").encode('utf-8'))

class Character:
	attr = None
	def __init__(self, path = "../settings/characters.json"):
		self.sampleData = {"charname":"","skills":[{"강타":0},{"막기":0}],"realuser":"","actions":[{"move":0}],"values":"","status":{"max_hp":0,"intelligent":0,"res_sturn":0,"health":0,"res_poison":0,"hp":0,"res_breath":0,"strength":0,"charisma":0,"res_parrelize":0,"level":1,"ac":0,"res_magicstaff":0,"class":"","res_magicspell":0,"res_death":0,"res_magicstic":0,"agillity":0,"wisdom":0}}
		self._path = path
		self.lib = d40lib.StdIOFile(path)
		self.jsonData = self.lib.jsonReturn()
		self.name = {}
		self.rtName = []
		self.getAllObject()

	def getAllObject(self):
		# for i in range(len(self.jsonData)):
		# 	if 'realuser' in self.jsonData[i]:
		# 		self.name[self.jsonData[i]['realuser']] = self.jsonData[i]
		for i in self.jsonData:
			if 'realuser' in self.jsonData[i]:
				self.name[self.jsonData[i]['realuser']] = self.jsonData[i]
			pass

		print(self.lib.Trans(self.name))
			
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

	def setObjtoName(self, obj, attribute = "", val1 = None):
		self.innerSetObj(obj, attribute, val1)
		self.name[obj["realuser"]] = obj
		# self.addUser()
		
	def innerSetObj(self, obj, attribute = "", val1 = None):
		try:
			for key in obj.keys():
				if(key == attribute):
					obj[key] = val1
				elif((type(obj[key]) is dict) or (type(obj[key]) is list)):
					self.innerSetObj(obj[key], attribute, val1)
					pass
		except:
			return None

	def addUsers(self):
		for key in self.name:
			self.rtName.append(self.name[key])

	def setBasicChar(self, charname, username, values, uclass):
		temp = self.sampleData
		self.setObjtoName(temp, "charname", charname)
		self.setObjtoName(temp, "realuser", username)
		self.setObjtoName(temp, "values", values)
		self.setObjtoName(temp, "class", uclass)
		self.name[username] = temp

	def printAllObject(self):
		for key in self.name.keys():
			print(key, self.name[key])

	def saveFile(self, path = "", name = ""):
		self.addUsers()
		self.lib.saveFile(path, name, self.name)
		
if __name__ == "__main__":
	a = Character("../settings/characters.json")
	# create user
	# a.setBasicChar("c", "c", "c", "c")
	# modfy user
	a.setObjtoName(a.getNameis("a"),"max_hp",100)
	a.saveFile(a._path,"")
	# print(a.getNameis("horo"))
	# print(a.getObjtoName("horo", "status"))
	# print(a.lib.Trans(a.rtName))
	# print(a.name)
	# a.setObjtoName(a.getNameis("horo"), "hp", 10)
	# # print(a.getObjtoName(a.getNameis("horo"), "hp"))
	# print(a.lib.Trans(a.getNameis("horo")))
	# print(a.name)
	# a.saveFile(a._path,"",a.rtName)