import d40lib
import pdb
import codecs
import sys, json, re

def printu(text):
	sys.stdout.buffer.write((text+"\n").encode('utf-8'))

class Character:
	def __init__(self, path = "../settings/characters.json"):
		self.lib = d40lib.StdIOFile(path)
		self.jsonData = self.lib.jsonReturn()
		self.charnames = {}
		# self.values = []
		# self.status = []
		# self.charclass = []
		# self.level = []
		# self.hp = []
		# self.ac = []
		# self.strength = []
		# self.intelligent = []
		# self.wisdom = []
		# self.agillity = []
		# self.health = []
		# self.charisma = []
		# self.res_poison = []
		# self.res_death = []
		# self.res_magicstic = []
		# self.res_parrelize = []
		# self.res_sturn = []
		# self.res_breath = []
		# self.res_magicspell = []
		# self.res_magicstaff = []
		# self.skills = []
		# self.actions = []
		# self.skillNames = []
		# self.actionNames = []
		self.getAllObject()

	def getAllObject(self):
		for i in self.jsonData:
			tmpname = i['charname']
			self.charnames[tmpname] = i
			# self.charname(tmpname) = i
			# self.values.append(i['values'])
			# self.status.append(i['status'])
			# self.charclass.append(i['class'])
			# self.level.append(i['level'])
			# self.hp.append(i['hp'])
			# self.ac.append(i['ac'])
			# self.strength.append(i['strength'])
			# self.intelligent.append(i['intelligent'])
			# self.wisdom.append(i['wisdom'])
			# self.agillity.append(i['agillity'])
			# self.health.append(i['health'])
			# self.charisma.append(i['charisma'])
			# self.res_poison.append(i['res_poison'])
			# self.res_death.append(i['res_death'])
			# self.res_magicstic.append(i['res_magicstic'])
			# self.res_parrelize.append(i['res_parrelize'])
			# self.res_sturn.append(i['res_sturn'])
			# self.res_breath.append(i['res_breath'])
			# self.res_magicspell.append(i['res_magicspell'])
			# self.res_magicstaff.append(i['res_magicstaff'])
			# self.skills.append(i['skills'])
			# self.actions.append(i['actions'])
			# self.skillNames.append(i[])
			# self.actionNames.append(i[])

	def ToJson(self):
		return self.jsonData

	def returnOfNameis(self, name = None):
		try:
			for key in self.charnames.keys():
				if key == name:
					return str(self.charnames[key]).replace("'","\"")
		except:
			return None

	def printAllObject(self):
		for key in self.charnames.keys():
			print(key, self.charnames[key])
		# print("values	:", self.values)
		# print("status	:", self.status)
		# print("class	:", self.charclass)
		# print("", self.level)
		# print("", self.hp)
		# print("", self.ac)
		# print("", self.strength)
		# print("", self.intelligent)
		# print("", self.wisdom)
		# print("", self.agillity)
		# print("", self.health)
		# print("", self.charisma)
		# print("", self.res_poison)
		# print("", self.res_death)
		# print("", self.res_magicstic)
		# print("", self.res_parrelize)
		# print("", self.res_sturn)
		# print("", self.res_breath)
		# print("", self.res_magicspell)
		# print("", self.res_magicstaff)
		# print("skills	:", self.skills)
		# print("ations	:", self.actions)
		# print("", self.skillNames)
		# print("", self.actionNames)


if __name__ == "__main__":
	a = Character("../settings/characters.json")
	a.printAllObject()


# self.charname = self.jsonData['charname']
# self.values = self.jsonData['values']
# self.status = self.jsonData['status']
# self.charclass = self.status['class']
# self.level = self.status['level']
# self.hp = self.status['hp']
# self.ac = self.status['ac']
# self.strength = self.status['strength']
# self.intelligent = self.status['intelligent']
# self.wisdom = self.status['wisdom']
# self.agillity = self.status['agillity']
# self.health = self.status['health']
# self.charisma = self.status['charisma']
# self.res_poison = self.status['res_poison']
# self.res_death = self.status['res_death']
# self.res_magicstic = self.status['res_magicstic']
# self.res_parrelize = self.status['res_parrelize']
# self.res_sturn = self.status['res_sturn']
# self.res_breath = self.status['res_breath']
# self.res_magicspell = self.status['res_magicspell']
# self.res_magicstaff = self.status['res_magicstaff']
# self.skills = self.jsonData['skills']
# self.actions = self.jsonData['actions']
# self.skillNames = []
# self.actionNames = []