import pdb
import codecs
import roominfo
import characters
import d40lib
import maps
import sys, json, re

def printu(text):
	sys.stdout.buffer.write((text+"\n").encode('utf-8'))

class Library(roominfo.SetRoom, maps.Maps):
	def __init__(self):
		self.RoomData = None
		self.MapData = None
		self.MobData = None
		pass

	def roomSetting(self, path = "./roominfo.json", mode = "auto"):
		self.RoomData = roominfo.Rooms(path)
		# self.roomfile = RoomData.lib
		self.roomJsonData = ""		
		if(mode == "auto"):
			self.RoomData.setAuto()
			self.roomJsonData = self.RoomData.jsonData
		else:
			pass

	def mapSetting(self, size = "3x3", mode = "auto"):
		self.MapData = maps.Maps(size)
		self.mapJsonData = ""
		if(mode == "auto"):
			self.MapData.createMaps()
			self.mapJsonData = self.MapData.ToJson()
		else:
			pass

	def mobSetting(self, path = "./characters.json", mode = "auto"):
		self.MobData = characters.Character(path)
		# self.mobfile = MapData.lib
		self.mobJsonData = ""
		if(mode == "auto"):
			self.mobJsonData = self.MobData.ToJson()
		else:
			pass


if __name__ == "__main__":
	a = Library()
	a.roomSetting("../settings/roominfo.json")
	a.RoomData.printAllObject()
	a.mapSetting("5x5")
	a.MapData.printMaptable()
	a.mobSetting("../settings/characters.json")
	a.MobData.printAllObject()
