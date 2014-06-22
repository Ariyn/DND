# -*- coding:utf-8 -*-

import pdb
import codecs
import roominfo
import characters
import d40lib
import maps
import items
import skill
import texts
import echo
import sys, json, re

def printu(text):
	sys.stdout.buffer.write((text+"\n").encode('utf-8'))

class librarys:
	def __init__(self):		
		self.RoomData = None
		self.MapData = None
		self.MobData = None
		self.CharData = None
		self.ItemData = None
		self.TextData = None
		self.SkillData = None
		self.echo = echo.echo()
		self.TwitterData = None
		pass

	def roomSetting(self, path = "../settings/roominfo.json", mode = "auto"):
		self.RoomData = roominfo.Rooms(path)
		# self.roomfile = RoomData.lib
		self.roomJsonData = ""		
		if(mode == "auto"):
			# self.RoomData.setAuto()
			self.roomJsonData = self.RoomData.jsonData
		else:
			pass

	def mapSetting(self, size = "3x3", floor = 1, mode = "auto", path = "../settings/"):
		self.MapData = maps.Maps(size, floor, path)
		self.mapJsonData = ""
		if(mode == "auto"):
			pass
			# self.MapData.completeMaps()
			# self.mapJsonData = self.MapData.ToJson()
		else:
			pass

	def mobSetting(self, path = "../settings/monsters.json", mode = "auto"):
		self.MobData = characters.Character(path)
		# self.mobfile = MapData.lib
		self.mobJsonData = ""
		if(mode == "auto"):
			pass
		else:
			pass

	def charSetting(self, path = "../settings/characters.json", mode = "auto"):
		self.CharData = characters.Character(path)
		self.charJsonData = ""
		if(mode == "auto"):
			pass
		else:
			pass

	def itemSetting(self, path = "../settings/items.json", mode = "auto"):
		self.ItemData = items.Items(path)
		self.itemJsonData = ""
		if(mode == "auto"):
			self.itemJsonData = self.ItemData.ToJson()
		else:
			pass

	def textSetting(self, path = "../settings/texts.json", mode = "auto"):
		self.TextData = texts.Texts(path)
		self.textJsonData = ""
		# if(mode == "auto"):
		# 	self.itemJsonData = self.ItemData.ToJson()
		# else:
		# 	pass

	def skillSetting(self, path = "../settings/skills.json", mode = "auto"):
		self.SkillData = skill.Skills(path)
		# self.roomfile = RoomData.lib
		self.SkillData = ""

if __name__ == "__main__":
	pass
	# Twitter sample
	# a = TwitterForm()
	# c = echo.echo()
	# d = librarys()
	# # data rcv

	# b = a.getRcvTwitInfo()
	# sys.stdout.buffer.write(str(b).encode("utf-8"))
	#print(bytes(b,"ISO-8859-1"))
	# result : [{'YuiDevelop': 'naoekfloidasfadklsm'}]

	# # data send
	# c.addEchoText("YuiDevelop", "nadonado")
	# c.addEchoText("hohohaha", "text")
	# a.Send(c.Message())
	# # result : Youngrae Jo ‏@ATLATCat01 36초
	# # 			@YuiDevelop nadonado

	# # c.echo()
	# # test = [[]]
	# # if len(test) == 1:
	# # 	print(test)

	a = librarys()
	a.roomSetting()
	a.RoomData.printAllObject()
	a.mapSetting("3x3", 2)
	a.MapData.printMaptable()
	a.mobSetting()
	a.MobData.printAllObject()
	a.charSetting()
	a.CharData.printAllObject()
	a.itemSetting()
	a.ItemData.printAllObject()
	#printu(str(a.TextData.jsonData))
