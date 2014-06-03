##parse_nature.py
# -*- coding:utf-8 -*-

import os, importlib, sys, json


class bModules(dict):
	lists = []

	def __init__(self, *args, **kwargs):
		dict.__init__(self, *args, **kwargs)
		self.__dict__ = self
		self.allowDotting()

	def allowDotting(self, state=True):
		if state:
			self.__dict__ = self
		else:
			self.__dict__ = dict()

	# def __init__(self, name = ""):
	# 	pass

	# def append(self, name, value):
	# 	print(self.__dict__)
	# 	self.__dict__[name] = value
	# 	#setattr(self, name, value)
	# 	self.lists.append(name)
	# def __set__(self, instance, value):


class oModules:
	jsonData = {}
	def __init__(self):
		_path = os.path.abspath("../")
		sys.path.append(_path)

	def setJson(self, ptype, path):
		path = os.path.abspath(path)
		self.jsonData[ptype] = json.loads(open(path,"r").read())

	def parseStart(self):
		packages = ["echo"]
		modules = [["echo"]]

		basicModules = bModules()
		for i in packages:
			mod = importlib.import_module(i)
			for e in modules[packages.index(i)]:
				temp = getattr(mod,e)
				#print(temp)
				basicModules[e] = temp

		modules = bModules()

		tempPackage = "scripts"
		packages = ["battle"]

		for i in packages:
			modules[i] = importlib.import_module(tempPackage+"."+i)

		print(modules.__dict__)
		print(basicModules.__dict__)
		#modules.battle.main(basicModules, None)
## 어디선가 파일을 불러온다.
## 이 json파일에서 분석할 python 파일의 위치를 입력받음.

if __name__ == "__main__":
	m = oModules()
	m.setJson('builtin','../scripts/builtin_method.json')
	m.parseStart()