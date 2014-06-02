# -*- coding:utf-8 -*-

import pdb
import codecs
import sys, json, re

def printu(text):
	sys.stdout.buffer.write((text+"\n").encode('utf-8'))

class Engine:
	jsonText, jsonData = "", {}

	functions = {
		"append":None,
		"next":None,
		"goto":None
	}

	#something like db
	gamedata = {
		"item":
		{
			"지도8":
			{
				"info":"문자 그대로 지도이다."
			}
		},
		"functions":{},
		"flag_map_search":[]
	}

	#player info
	playerdata ={}

	def __init__(self, path = ".", sample = "no"):

		if sample == "yes":
			self.path = "sample.json"
		else:
			self.path = path
		#self.file = codecs.open(self.path,'r',"utf8")


	def readFile(self):
		for lines in self.file:
			self.jsonText += lines
			#sys.stdout.buffer.write(lines.encode('utf8'))

	def parseFile(self):
		self.readFile()
		self.jsonData = json.loads(s=self.jsonText)
		self.init()

	def init(self):
		self.playerdata["roomNumber"] = 0

	def run(self):
		self.playerdata["roomNumber"] = 0
	
	def parseFlag(self, key, val = None):
		
		split_key = self._split_key(key)

		retval = None
		if len(split_key) == 2:
			if split_key[0][0] != "&":
				pass
			else:
				flag = [split_key[0][1:],None]

				if split_key[1][1:] == "room_number":
					flag[1] = self.playerdata["roomNumber"]
				elif split_key[1][1:] == "flag_always":
					flag[1] = "True"
				else:
					flag[1] = split_key[1]

				if flag[0] == "flag_map_search":
					if flag[1] is "True":
						retval = True
					elif flag[1] in self.gamedata[flag[0]]:
						retval = True
					else:
						retval = False
				elif flag[0] == "prompt":		
					if self.playerdata["prompt"] == flag[1].split("\"")[1]:
						retval = True
					else:
						retval = False
				else:
					retval = False
			return retval

		elif len(split_key) == 1:
			if val[0] == "(" and val[1] == "*" and val[-1] == ")":
				self.func(key, val[2:-1])
		return retval

	def func(self, target = None, func = None):
		innerString = re.findall("\".+\"",func)
		if innerString:
			test = re.sub("\".+\"","&sub",func)
			test = test.split(" ")
			func = [x if x != "&sub" else innerString for x in test]

		split_func = func.split(" ")
		if split_func[0] == "append":
			if target not in self.gamedata:
				self.gamedata[target] = []
			try:
				split_func[1] = int(split_func[1])
			except ValueError:
				pass
			self.gamedata[target].append(split_func[1])

		elif split_func[0] == "prompt":
			text = input()
			self.playerdata[target] = text

		elif split_func[0] == "next":
			for i in self.playerdata["room"]["next"]:
				result = self.parseFlag(i[0],i[1])
				if result is True:
					print("tests")
					retval, val = self.func(func=i[1][2:-1])
					if retval == "goto":
						return retval, val

		elif split_func[0] == "goto":
			return "goto", split_func[1]

		elif split_func[0] in self.gamedata["functions"]:
			for i in self.gamedata["functions"][split_func[0]]:
				result = self.parseFlag(i[0],i[1])
				if result is True:
					return self.textFunc(i[1])
				else:
					pass

	def textFunc(self, text):
		_funcs = []

		for i in self.gamedata["functions"]:
			if "(*"+i+")" in text:
				result = self.func(func = i)
				if result:
					text = text.replace("(*"+i+")", result)

		if "(*next)" in text:
			_funcs.append("next")
			selects = self.nextSelections()
			text = text.replace("(*next)","")
			text += selects

		if "(*prompt)" in text:
			_funcs.append("prompt")
			text = text.replace("(*prompt)","")

		printu(text)

		for i in _funcs:
			#pdb.set_trace()
			val, data = self.func(func = i)
			if val == "goto":
				self.clearSelfData()
				self.playerdata["roomNumber"] = data
				return 0

	def nextSelections(self):
		retval = ""
		for i in self.playerdata["room"]["next"]:
			_retval = re.findall("\".+\"",i[0])
			if len(_retval) >= 1:
				retval += _retval[0]+"\n"

		return retval

	def clearSelfData(self):
		#self.playerdata["prompt"] = ""
		#self.playerdata["room"] = None
		pass

	@staticmethod
	def _split_key(key):
		innerString = re.findall("\".+\"",key)
		if innerString:
			test = re.sub("\".+\"","&sub",key)
			test = test.split(" ")
			split_key = [x if x != "&sub" else innerString[0] for x in test]
		else:
			split_key = key.split(" ")

		return split_key
			

eng = Engine(sample = "yes")
#eng.parseFile()

eng.init()
eng.playerdata["room"] = {"next":{}}
eng.playerdata["room"]["next"] = [["&flag_map_search &room_number","(*goto 52)"],
				["prompt","(*prompt)"],
				["&prompt \"문을 연다\"","(*goto 66)"],
				["&prompt \"돌아 간다\"","(*goto 37)"]]

eng.gamedata["functions"]["action-1"] = [["&flag_map_search &room_number","당신은 이미 이곳을 탐험했다. (*next)"]]
eng.gamedata["functions"]["action-1"].append(["&flag_map_search &flag_always","이 방의 북쪽 벽에서 3m를 나가서 왼쪽(서쪽)으로 틀고, 거기서 3m를 더 가면 새로운 방이 나타난다. 이곳에는 고블린들이 더 있다. 어떻게 하겠는가?\n(*next)"])
# #eng.parseFlag("flag_map_search","(*append 0)")
eng.textFunc("(*action-1)")

#eng.textFunc("(*action-1)")

#if eng.parseFlag("&flag_map_search &room_number") == True:
#	eng.textFunc("당신은 이미 이곳을 탐험했다. (*next)")







