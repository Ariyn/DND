##parse_nature.py
# -*- coding:utf-8 -*-

import os, importlib, sys, json

def print(*text):
	sys.stdout.buffer.write((str(text)+"\n").encode('utf-8'))


class bModules(object):
	def __init__(self, *args, **kwargs):
		pass

	def __setattr__(self, name, value):
		try:
			super(bModules, self).__setattr__(name, value)
		except AttributeError:
			pass
			#super(bModules, self).__setattr__(name, value)

	def __getattr__(self, name):
		try:
			temp = super(bModules, self).__getattribute__(name)
		except AttributeError:
			super(bModules, self).__setattr__(name, bModules())
			temp = super(bModules, self).__getattribute__(name)
		return temp

class oModules:
	jsonData = {}
	realModules = {}
	def __init__(self):
		_path = os.path.abspath("./lib")
		sys.path.append(_path)
		pass

	def parseStart(self):
		modules = ["echo","librarys"]
		methods = [["echo", "addEchoText"],["roomSetting","mapSetting","mobSetting","charSettting","itemSetting", "textSetting"]]

		basicModules = bModules()
		for i, moduleId in zip(modules, methods):
			mod = importlib.import_module(i)
			
			print(mod, i)
			temp = getattr(mod,i)()
			for e in moduleId:
				basicModules.__setattr__(e,getattr(temp, e))

		self.realModules[i] = temp

		modules = bModules()

		packages = ["battle", "main"]

		for i in packages:
			print(i)
			modules.__setattr__(i,importlib.import_module("scripts."+i))

		return modules, basicModules
		#modules.battle.main(basicModules, None)
## 어디선가 파일을 불러온다.
## 이 json파일에서 분석할 python 파일의 위치를 입력받음.

def runModules():
	pass

if __name__ == "__main__":
	m = oModules()
	#data = bModules()
	
	data = {"player":{"synario":"놀람","script":-1}, "flag_battle":False}
	
	#m.setJson('builtin','../scripts/builtin_method.json')

	modules, basicModules = m.parseStart()
	
	data = modules.main.main(basicModules, data)

	if data["flag_battle"]:
		modules.battle.main(basicModules, data)

	#print(dir(basicModules))
	basicModules.roomSetting("settings/roominfo.json")
	m.realModules["lib"].RoomData.printAllObject()
	basicModules.mapSetting("3x3", 2, path="settings/")
	m.realModules["lib"].MapData.printMaptable()
	basicModules.mobSetting(path = "settings/monsters.json")
	m.realModules["lib"].MobData.printAllObject()
	basicModules.charSettting(path ="settings/characters.json")
	m.realModules["lib"].CharData.printAllObject()
	basicModules.itemSetting(path = "settings/items.json")
	m.realModules["lib"].ItemData.printAllObject()
	#basicModules.mapSetting("settings/characters.json")
