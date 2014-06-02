# -*- coding:utf-8 -*-

import codecs
import sys, json

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
		"functions":{}
	}

	#player info
	playerdata ={}

	def __init__(self, path = ".", sample = "no"):

		if sample == "yes":
			self.path = "sample.json"
		else:
			self.path = path
		self.file = codecs.open(self.path,'r',"utf8")


	def readFile(self):
		for lines in self.file:
			self.jsonText += lines
			#sys.stdout.buffer.write(lines.encode('utf8'))

	def parseFile(self):
		self.readFile()
		self.jsonData = json.loads(s=self.jsonText)

	def run(self):
		room = 0
		
		_data = self.jsonData[room]

		key = "action"
		for akey in _data[key]:
			if akey == "onEnter":
				for i in _data[key][akey]:
					printu(i+" "+_data[key][akey][i])
					self.parseFunc(i,_data[key][akey][i])
			elif akey != "coment" and akey != "next":
				self.gamedata["functions"][akey] = {}
				for i in _data[key][akey]:
					self.gamedata["functions"][akey][i] = _data[key][akey][i]
		
		key = "text"
		self.text(_data[key])

	def checker(self, target, data):
		pass

	def parseFunc(self, target = None, pFunc = None):
		if pFunc[0] == "(" and pFunc[1] == ")":
			pFunc = pFunc[1:-1]
		func = pFunc.split(" ")
		retval = None
		if len(func) == 2:
			printu(func[0])
			printu(func[1])
			if func[0][0] == "*" and func[0][1:] in self.functions:
				retval = self.functions[func[0][1:]](target = target, data = func)

			elif func[0][0] == "*" and func[0][1:] in self.gamedata["functions"]:
				self.userFunc(func[0][1:])

			elif func[0][0] == "&" and func[1][0] == "&":
				
				self.parseFlag(pFunc)
			else:
				pass
				#error

		elif len(func) == 1:
			if func[0][1:] in self.functions:
				retval = self.functions[func[0][1:]]()

			elif func[0][1:] in self.gamedata["functions"]:
				self.userFunc(func[0][1:])
			else:
				printu(func[0])

		if retval is not None:
			return retval

	def userFunc(self, func = None, data = None):
		retval = None

		if func in self.gamedata["functions"]:
			for i in self.gamedata["functions"][func]:
				retval = self.parseFlag(i)

		if retval:
			pass


	def append(self, target, data):
		if target not in self.playerdata:
				self.playerdata[target] = []

		if "flag" in target:
			self.playerdata[target].append(data[1])
		elif target == "items":
			self.playerdata["items"].append(
				self.gamedata["item"][data[1]])

		return True

	def next(self, pTarget, data):
		if pTarget[0] == "&":
			target = pTarget.split(" ")
		else:
			pass


	def goto(self, target, data):
		pass

	def prompt(self, target, data):
		pass

	def text(self, data):
		for i in self.gamedata["functions"]:
			if "(*"+i+")" in data:
				self.parseFunc(pFunc = "*"+i)

#"&flag_map_search &room_number":"(*action-1)",
	def parseFlag(self, data):
		datas = data.split(" ")
		if datas[0][0] != "&" and datas[1][0] != "&":
			print("error")
			pass
			#error
		else:
			printu(datas[0][1:])
			flag = datas[0][1:]
			print("test")
			if flag == "flag_map_search":
				if self.gamedata[flag]:
					print(self.gamedata[flag])


	# def _parseFile(self, data):
	# 	num = 0
	# 	for key in data:
	# 		#key = types.keys()
	# 		if key == "number":
	# 			num = data[key]
	# 			self.roomdata[num] = {}
	# 		elif key == "text":
	# 			self.roomdata[num]["text"] = data[key]
	# 		elif key == "action":
	# 			for akey in data[key]:
	# 				if akey == "__init__":
	# 					pass
	# 				elif akey == "next":
	# 					for nkey in data[key][akey]:

	# 				elif akey == "coment":
	# 					pass
	# 				else:
	# 					pass


#old data type
#"flag_map_search":"(*append 9)",

#new data type
#"&flag_map_search &room_number":"flag_map_search 9",

eng = Engine(sample = "yes")
eng.functions["append"] = eng.append
eng.functions["next"] = eng.next
eng.functions["goto"] = eng.goto
eng.functions["prompt"] = eng.prompt
eng.functions["text"] = eng.text

eng.parseFile()

eng.run()