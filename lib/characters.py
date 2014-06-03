import d40lib
import pdb
import codecs
import sys, json, re

def printu(text):
	sys.stdout.buffer.write((text+"\n").encode('utf-8'))

class Character:
	def __init__(self, path = "./characters.json"):
		self.lib = d40lib.StdIOFile(path)
		self.jsonData = self.lib.jsonReturn()
		self.getAllObject()

	def getAllObject(self):
		self.charname = self.jsonData['charname']
		self.values = self.jsonData['values']
		self.status = self.jsonData['status']
		self.charclass = self.status['class']
		self.level = self.status['level']
		self.hp = self.status['hp']
		self.ac = self.status['ac']
		self.strength = self.status['strength']
		self.intelligent = self.status['intelligent']
		self.wisdom = self.status['wisdom']
		self.agillity = self.status['agillity']
		self.health = self.status['health']
		self.charisma = self.status['charisma']
		self.res_poison = self.status['res_poison']
		self.res_death = self.status['res_death']
		self.res_magicstic = self.status['res_magicstic']
		self.res_parrelize = self.status['res_parrelize']
		self.res_sturn = self.status['res_sturn']
		self.res_breath = self.status['res_breath']
		self.res_magicspell = self.status['res_magicspell']
		self.res_magicstaff = self.status['res_magicstaff']
		self.skills = self.jsonData['skills']
		self.actions = self.jsonData['actions']
		self.skillNames = []
		self.actionNames = []

	def ToJson(self):
		return self.jsonData

	def printAllObject(self):
		print("charname	:", self.charname)
		print("values	:", self.values)
		print("status	:", self.status)
		print("class	:", self.charclass)
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
		print("skills	:", self.skills)
		print("ations	:", self.actions)
		# print("", self.skillNames)
		# print("", self.actionNames)


if __name__ == "__main__":
	a = Monster("../settings/characters.json")
	print(a.jsonData)