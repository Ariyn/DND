import json
import codecs
import sys, re
from random import choice

def printu(text):
	sys.stdout.buffer.write((text+"\n").encode('utf-8'))

class D40Map:
	def __init__(self):
		self.Value = []
		self.South = False
		self.North = False
		self.West = False
		self.East = False
		self.Up = False
		self.Down = False
		self.Number = None
		self.ConCT = 0
		self.jsonData = ""
		self.Floor = 0
		pass

	def setting(self, string, jstring = None):
		try:
			if string == "North":
				self._callNorth()
			elif string == "South":
				self._callSouth()
			elif string == "West":
				self._callWest()
			elif string == "East":
				self._callEast()
			elif string == "Up":
				self._callUp()
			elif string == "Down":
				self._callDown()
			else:
				print("input correct!\n")
			self.jsonData = jstring
		except:
			pass

# connection funcs
	def _callNorth(self):
		self.North = True
		if("North" not in self.Value):
			self.Value.append("North")
			self.ConCT += 1

	def _callSouth(self):
		self.South = True
		if("South" not in self.Value):
			self.Value.append("South")
			self.ConCT += 1

	def _callWest(self):
		self.West = True
		if("West" not in self.Value):
			self.Value.append("West")
			self.ConCT += 1

	def _callEast(self):
		self.East = True
		if("East" not in self.Value):
			self.Value.append("East")
			self.ConCT += 1

	def _callUp(self):
		self.Up = True
		if("Up" not in self.Value):
			self.Value.append("Up")

	def _callDown(self):
		self.Down = True
		if("Down" not in self.Value):
			self.Value.append("Down")

	def returnJson(self):
		self.jsonData = "{\"Number\":" + str(self.Number).replace("'","") +",\"connections\":"+ str(self.Value).replace("'","\"") + "}"
		return self.jsonData

# end connection func


if __name__ == "__main__":
	b = ["North", "South", "West", "East", "UP", "Down"]
	c = choice(b)
	a = d40Map()
	a.setting(c)
	print(c, a.Value)