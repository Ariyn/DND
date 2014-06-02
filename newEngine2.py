# -*- coding:utf-8 -*-

import pdb
import codecs
import sys, json, re

def printu(text):
	sys.stdout.buffer.write((text+"\n").encode('utf-8'))

class Engine:
	datas = {
		"playerdata" :
		{

		},
		"gamedata" :
		{
			"funcs":{},
			"flag_private_next":False,
			"flag_private_goto":False,
			"flag_private_restart":False
		}
	}
	jsonText = ""
	def __init__(self, path = "", sample = "no"):

		if sample == "yes":
			self.path = "/Users/minuk-hwang/Documents/Pythons/DND/sample.json"
		else:
			self.path = path
		self.file = codecs.open(self.path,'r',"utf8")


	def readFile(self):
		for lines in self.file:
			self.jsonText += lines
			#sys.stdout.buffer.write(lines.encode('utf8'))

	def parseFile(self):
		self.readFile()
		#printu(self.jsonText)
		self.jsonData = json.loads(s=self.jsonText)
		self.init()

	def init(self):

		self.datas["playerdata"]["roomNumber"] = 0

	def run(self):
		self._parseFile()
		#printu(self.jsonData[self.datas["playerdata"]["roomNumber"]]["text"])

		#printu("events = "+str(self.datas["playerdata"]["events"]))
		self.flagParse("temp_room_number","(*set "+str(self.datas["playerdata"]["roomNumber"])+")")
		#eng.flagParse("flag_map_search","(*append 0)")
		if "onEnter" in self.datas["playerdata"]["events"] and len(self.datas["playerdata"]["events"]["onEnter"]) != 0:
			self.runActions("onEnter")
		run = True
		#self.textFunction(self.jsonData[self.datas["playerdata"]["roomNumber"]]["text"])
		while(run):
			data = self.textFunction("text",self.jsonData[self.datas["playerdata"]["roomNumber"]]["text"])
			printu(data)

			if self.datas["gamedata"]["flag_private_next"]:
				self.runActions("next")
			if self.datas["gamedata"]["flag_private_goto"]:
				print("goto")
			if not self.datas["gamedata"]["flag_private_restart"]:
				run = False

	def _parseFile(self):
		self.datas["playerdata"]["events"] = self.jsonData[self.datas["playerdata"]["roomNumber"]]["action"]


		# for i in self.jsonData[self.datas["playerdata"]["roomNumber"]]["action"]:
		# 	if i == "coment":
		# 			continue
		# 	for e in self.jsonData[self.datas["playerdata"]["roomNumber"]]["action"][i]:
		# 		print(e,i)
		# 		self.datas["playerdata"]["events"][i] = []
		# 		self.datas["playerdata"]["events"][i].append([e,self.jsonData[self.datas["playerdata"]["roomNumber"]]["action"][i][e]])

	def runActions(self, key):
		#print("key",key)
		_retdata = ""
		if key in self.datas["playerdata"]["events"]:
			for i in self.datas["playerdata"]["events"][key]:
				done, text = self.flagParse(i[0],i[1])
				if done == True:
					_retdata = text#i[1]
					break
		return _retdata
		pass

	def checkFlag(self, split_key):
		pass

	def flagParse(self, key, vals):
		split_key = self.splitKey(key)
		isRunFunc = False

		dataKey = None
		_database = None

		if len(split_key) == 0:
			pass #error

		elif len(split_key) == 1:
			if "&" in key:
				pass #error
			else:
				db = self.checkData(key)
				isRunFunc = True
				dataKey = key
				_database = db

		elif len(split_key) == 2:
			#print(split_key)
			db = [self.checkData(split_key[0]),self.checkData(split_key[1])]
			_option = None

			#print(db,split_key)
			#checkFlag
			if db[0] == None:
				_database = db[1]
				_dataParm = [self.datas[db[1]][split_key[1][1:]],split_key[0]]
				#print(_dataParm)
			elif db[1] == None:
				_database = db[0]
				_dataParm = [split_key[1],self.datas[db[0]][split_key[0][1:]]]
				#print(_dataParm)

			# elif split_key[0][0] == "&" and split_key[1][0] != "&":
			# 	_dataParm = [db[1][split_key[1][1:]],db[0][split_key[0]]]
			# 	#compare = self._compareFunc([db[1][split_key[1][1:]],db[0][split_key[0]]])

			# elif split_key[0][0] != "&" and split_key[1][0] == "&":
			# 	pass
			elif split_key[0] == "&flag_always":
				_dataParm = [self.datas[db[1]][split_key[1][1:]],split_key[0]]
			elif split_key[1] == "&flag_always":
				_dataParm = [split_key[1],self.datas[db[0]][split_key[0][1:]]]
			elif split_key[0][0] == "&" and split_key[1][0] == "&":
				#compare = self._compareFunc([db[1][split_key[1][1:]],db[0][split_key[0][1:]]])
				_dataParm = [self.datas[db[1]][split_key[1][1:]],self.datas[db[0]][split_key[0][1:]]] 
			compare = self._compareFunc(_dataParm, _option)
			if compare is None:
				pass #error
			elif compare is True:
				isRunFunc = True
				#print(dataKey, vals, _database)
				pass #runFunctions
			elif compare is False:
				pass #doesn't run
			else:
				pass #error
		elif len(split_key) == 3:
			pass

		retData, _retData = "", ""
		if isRunFunc is True:
			#result, action, data  = self.runFunction(key = dataKey, val = vals, db = _database)
			_retData = self.textFunction(key = dataKey, val = vals, db = _database)
			#printu("pruntu"+ retData)
			#printu("flagParser"+_retData)
			if _retData == "set" or _retData == "append":
				retData = False
			else:
				retData = True

		return retData, _retData
			# if action == "append":
			# 	db[key].append(data)
			# elif action =="set":
			# 	db[key] = data

	def _compareFunc(self, data, option = None):
		isIn = None
		#print(data)
		if data[0] == "&flag_always" or data[1] == "&flag_always":
			isIn = True
		elif type(data[0]) == list:
			if type(data[1]) == list:
				datas = list(set(data[0]).intersection(data[1]))
				if len(datas) == 0:
					isIn = False
				else:
					isIn = True
			else:
				if data[1] in data[0]:
					isIn = True
				else:
					isIn = False
		else:
			if type(data[1]) == list:
				if data[0] in data[1]:
					isIn = True
				else:
					isIn = False
			else:
				if data[0] == data[1]:
					isIn = True
				else:
					isIn = False
		return isIn

	def textFunction(self, key = None, val = None, db= None):
		#printu(val)
		actions = re.findall("(\(\*[^(]+\))", val)
		text = val
		#(\(\*\S+\)
		#print(len(actions))
		for i in actions:
			#printu("action "+i)
			#printu("action "+text)
			#printu(str(key))
			retData = self.runFunction(key = key, val = i, db = db)
			text = text.replace(i,retData)
		
		#printu("end "+text)
		return text
		
	def runFunction(self, key = None,  val = None, db = None):
		_retval = ""
		result = None

		if key is None:#if states true
				#printu(val)
			#if val[0] == "(" and val[-1] == ")" and val[1] == "*":
				name = val[2:-1].split(" ")
				if name[0] in self.datas["gamedata"]["funcs"]:
					#print(name[0])
					if len(name) == 2:
						_inputData = {"key":key,"value":name[1]}
						result, action, data = self.datas["gamedata"]["funcs"][name[0]](self = self, data = _inputData)
					elif len(name) == 1:
						result, action, data = self.datas["gamedata"]["funcs"][name[0]](self = self)
				elif name[0] in self.datas["playerdata"]["events"]:#somewhere store event datas
					#print(name[0])
					_retval = self.runActions(name[0])
					#printu("retdata"+_retval)
			#else:
			#	pass
		else:#run functions with parameters
			#if val[0] == "(" and val[-1] == ")" and val[1] == "*":
				name = val[2:-1].split(" ")
				if name[0] in self.datas["gamedata"]["funcs"]:
					#print(name[0])
					if len(name) == 2:
						_inputData = {"db":db,"key":key,"value":name[1]}
						result, action, data = self.datas["gamedata"]["funcs"][name[0]](self = self, data = _inputData)
					elif len(name) == 1:
						_inputData = {"db":db,"key":key}
						result, action, data = self.datas["gamedata"]["funcs"][name[0]](self = self, data = _inputData)
				elif name[0] in self.datas["playerdata"]["events"]:#somewhere store event datas
					_retval = self.runActions(name[0])

				if result != None:
					_retval = action
					if action == "append":
						self.datas[_inputData["db"]][_inputData["key"]].append(data)
					elif action == "set":
						#printu(data)
						self.datas[_inputData["db"]][_inputData["key"]] = data
		#printu(_retval)
		return _retval
		pass

	def checkData(self, key):
		_database = None
		try:
			key = int(key)
		except ValueError:
			if "\"" in key[0] or "\"" in key[0]:
				_database = None
			else:
				if "flag" in key or key in self.datas["gamedata"]:
					if key[0] == "&":
						if key[1:] not in self.datas["gamedata"]:
							self.datas["gamedata"][key[1:]] = None
					else:
						if key not in self.datas["gamedata"]:
							self.datas["gamedata"][key] = None
					_database = "gamedata"
				elif "temp" in key or key in self.datas["playerdata"]:
					if key[0] == "&":
						if key[1:] not in self.datas["playerdata"]:
							self.datas["playerdata"][key[1:]] = None
					else:
						if key not in self.datas["playerdata"]:
							self.datas["playerdata"][key] = None
					_database = "playerdata"

		# print(_database)
		return _database

	@staticmethod
	def splitKey(key):
		innerString = re.findall("\".+\"",key)
		if innerString:
			test = re.sub("\".+\"","&sub",key)
			test = test.split(" ")
			split_key = [x if x != "&sub" else innerString[0] for x in test]
		else:
			split_key = key.split(" ")


		return split_key

def _prompt(self, data = None, option = ""):
	#return input(option)
	#testFunction
	#result, action, data
	retData = input(option)
	try:
		retData = int(retData)
	except ValueError:
		retData = "\""+retData+"\""
	return True, "set", retData

def _append(self, data = None, option = ""):
	# print(data)
	if type(self.datas[data["db"]][data["key"]]) != "list" or type(self.datas[data["db"]][data["key"]]) != "array":
		_data = self.datas[data["db"]][data["key"]]
		del self.datas[data["db"]][data["key"]]
		self.datas[data["db"]][data["key"]] = [_data]

	#data["db"][data["key"]].append(data["value"])
	return True, "append", data["value"]

def _set(self, data = None, option = ""):
	if type(self.datas[data["db"]][data["key"]]) == "list" or type(self.datas[data["db"]][data["key"]]) == "array":
		return False, None, None
	else:
		return True, "set", data["value"]
def _goto(self, data = None, option = ""):
	self.datas["gamedata"]["flag_private_next"] = False
	self.datas["gamedata"]["flag_private_goto"] = data["value"]
	self.datas["gamedata"]["flag_private_restart"] = False
	self.runActions("onExit")

	return True, "goto", ""

def _next(self, data = None, option = ""):
	self.datas["gamedata"]["flag_private_next"] = True
	return True, "", ""

def _restart(self, data = None, option = ""):
	#print("restart")
	self.datas["gamedata"]["flag_private_restart"] = True
	return True, "", ""


eng = Engine(sample = "yes")
eng.parseFile()

eng.datas["gamedata"]["funcs"]["prompt"] = _prompt
eng.datas["gamedata"]["funcs"]["append"] = _append
eng.datas["gamedata"]["funcs"]["next"] = _next
eng.datas["gamedata"]["funcs"]["set"] = _set
eng.datas["gamedata"]["funcs"]["goto"] = _goto
eng.datas["gamedata"]["funcs"]["restart"] = _restart

eng.run()