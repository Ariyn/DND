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
import TwitterEngine
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

class TwitterForm:
	def __init__(self, path = "../settings/twitterData.json"):
		self._path = path
		self.rtv = {}
		self.lib = d40lib.StdIOFile("../settings/usermsg.json")
		self.lib.parseFile()
		self.infodata = []
		self.TMData = TwitterEngine.Twitter_Manager(path)
		# self.DND = TwitterEngine.DND_Twitter(path)

	def checkJson(self):
		if len(self.lib.jsonData) <= 0:
			self.lib.saveFile(self.lib.path,"","[]")
		else:
			self.infodata = self.lib.jsonReturn()

	def getRcvTwitInfo(self):
		self.message = self.TMData.receiveMessagePerID()
		# self.message = [{'created_at': 'Fri Jun 20 08:51:23 +0000 2014', 'text': '@ATLATCat01 naoekfloidasfadklsm', 'screen_name': 'YuiDevelop', 'id': '2560618506'}]
		# print(self.message)
		try:
			for j in range(len(self.message)):
				temp1 = ""
				temp2 = ""
				self.rtv = {}
				for i in self.message[j]:
					if i == "screen_name":
						temp1 = self.message[j][i]
					elif i == "text":
						temp2 = self.message[j][i]
						temp2 = temp2[temp2.find(" ")+1:]
				self.rtv[temp1] = temp2
				self.infodata.append(self.rtv)
				# self.lib.saveFile(self.lib.path,"",self.infodata)
				# self.checkJson()
		except:
			print("no data")
			return None

		return self.infodata

	def Send(self, userinfo):
		self.TMData.sendMessages(userinfo)
				

if __name__ == "__main__":
	
	# # Twitter sample
	# a = TwitterForm()
	# c = echo.echo()
	# d = librarys()
	# # data rcv

	# b = a.getRcvTwitInfo()
	# sys.stdout.buffer.write(str(b).encode("utf-8"))
	# #print(bytes(b,"ISO-8859-1"))
	# # result : [{'YuiDevelop': 'naoekfloidasfadklsm'}]

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
	a.charSettting()
	a.CharData.printAllObject()
	a.itemSetting()
	a.ItemData.printAllObject()
	
	#printu(str(a.TextData.jsonData))
