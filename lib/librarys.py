import pdb
import codecs
import roominfo
import characters
import d40lib
import maps
import items
import texts
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
			self.mobJsonData = self.MobData.ToJson()
		else:
			pass

	def charSettting(self, path = "../settings/characters.json", mode = "auto"):
		self.CharData = characters.Character(path)
		self.charJsonData = ""
		if(mode == "auto"):
			self.charJsonData = self.CharData.ToJson()
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
		if(mode == "auto"):
			self.itemJsonData = self.ItemData.ToJson()
		else:
			pass

if __name__ == "__main__":
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
	a.textSetting()
	#printu(str(a.TextData.jsonData))