#!/usr/bin/env python
# -*- coding:utf-8 -*-

import lib.jsonParse
import lib.newTwitterEngine
from lib.dice import dice
import lib.monster

import parse_nature

class DND:
	def testTwit(self, characters):
		text = {}
		for i in characters:
			text[i] = input(i+"의 입력\n")

		return text

	def main(self):
		m = parse_nature.oModules()
			#data = bModules()
			
		self.data = {
			"players":
			{
				"YuiDevelop":{"character":"miko","synario":"기본","location":83,"flag_battle":False,"moveEvent":[]},
				"MuTopia_ArtTeam":{"character":"horo","synario":"기본","location":0,"flag_battle":False,"moveEvent":[]}
			},
			"texts":{},
			"characters":{},
			"rooms":{}
		}

		tf = lib.newTwitterEngine.DND_Twitter("settings/oauth.json")
		#m.setJson('builtin','../scripts/builtin_method.json')

		modules, basicModules = m.parseStart()

		print(m.realModules["librarys"])

		basicModules.TwitterData = tf
		basicModules.echoTwitterSetting(tf)
		#print(dir(basicModules))
		basicModules.roomSetting("settings/roominfo.json")
		# m.realModules["librarys"].RoomData.printAllObject()
		basicModules.mapSetting("3x3", 2, path="settings/")
		# m.realModules["librarys"].MapData.printMaptable()
		basicModules.mobSetting(path = "settings/monsters.json")
		# m.realModules["librarys"].MobData.printAllObject()
		basicModules.charSettting(path ="settings/characters.json")
		# m.realModules["librarys"].CharData.printAllObject()
		basicModules.itemSetting(path = "settings/items.json")
		# m.realModules["librarys"].ItemData.printAllObject()
		basicModules.textSetting(path = "settings/texts.json")

		basicModules.skillSetting(path = "settings/skills.json")
		
		self.basicModules = basicModules
		self.modules = modules
		self.tf = tf

		#data["players"] = #player json parse
		self.data["monster"] = lib.monster.monster
		self.data["rooms"] = m.realModules["librarys"].RoomData.name
		self.data["monsters"] = m.realModules["librarys"].MobData.name
		self.data["characters"] = m.realModules["librarys"].CharData.name
		self.data["texts"] = m.realModules["librarys"].TextData.jsonData

		#print("bd", self.data)

		#print(m.realModules["librarys"].RoomData.number)
		#print(m.realModules["librarys"].)

		num = 3
		while num > 0:
			num-=1

			#retInputData = basicModules.TwitterData.getRcvTwitInfo()
			retInputData = self.testTwit(self.data["players"].keys())

			newUserData = self.checkNewUser()
			print("\n")
			for i in self.data["players"]:
				if i not in retInputData:
					continue

				#print(self.data["characters"])
				characterData = self.data["characters"][i]
				#[self.data["characters"][x] for x in self.data["characters"] if x == self.data["players"][i]["character"]]
				
				if self.data["players"][i]["flag_battle"]:
					options = modules.battle.main(
						basicModules,
						self.data["players"][i],
						{
							"player"	:	i,
							"characters":	characterData,
							"rooms"		:	self.data["rooms"],
							"texts"		:	self.data["texts"],
							"monsters"	:	self.data["monsters"],
							"inputs"	:	retInputData[i],
							"monster"	:	self.data["monster"]
						})
				else:
					#print(characterData)
					# if len(characterData) < 1:
					# 	pass # not played yet
					# else:
					# 	characterData = characterData[0]

					options = modules.main.main(
						basicModules,
						self.data["players"][i],
						{
							"player"	:	i,
							"characters":	characterData,
							"rooms"		:	self.data["rooms"],
							"texts"		:	self.data["texts"],
							"monsters"	:	self.data["monsters"],
							"monster"	:	self.data["monster"],
							"inputs"	:	retInputData[i]
						})
				if options:
					if "move" in options:
						self.data["players"][i]["location"] = options["move"]
					if "state" in options:
						print(options["state"])
					if "event" in options:
						if options["event"] == "demage":
							_demages = dice(options["demage"])[0]
							m.realModules["librarys"].CharData.setObjtoName(
								m.realModules["librarys"].CharData.getNameis(self.data["players"][i]["character"]), "hp", _demage)
							pass
						elif options["event"] == "battle":
							self.data["players"][i]["flag_battle"] = True
							self.data["players"][i]["monster"] = options["monster"]
						elif options["event"] == "synario":
							self.data["players"][i]["flag_battle"] = False

					self.data["players"][i]["moveEvent"] = options["moveEvent"]

			basicModules.echo()
			#wait 20sec

			# if "flag_battle" in options:
			# 	self.data[i]["flag_battle"] = options["flag_battle"]

	def checkNewUser(self):
		follower = self.tf.getUsers()
		for i in [x for x in follower if x not in self.data["players"]]:
			print(i)

		pass

if __name__ == "__main__":
	d = DND()
	d.main()




