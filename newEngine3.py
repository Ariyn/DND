# -*- coding:utf-8 -*-

import lib.jsonParse
import lib.echo
from lib.dice import dice
import lib.monster

import parse_nature

def testTwit(characters):
	text = {}
	for i in characters:
		text[i] = input(i+"의 입력\n")

	return text

def main():
	m = parse_nature.oModules()
		#data = bModules()
		
	data = {
		"players":
		{
			"YuiDevelop":{"character":"miko","synario":"기본","location":83,"flag_battle":False,"moveEvent":[]},
			"MuTopia_ArtTeam":{"character":"horo","synario":"기본","location":0,"flag_battle":False,"moveEvent":[]},
		},
		"texts":{},
		"characters":{},
		"rooms":{}
	}

	#m.setJson('builtin','../scripts/builtin_method.json')

	modules, basicModules = m.parseStart()

#	print(m.realModules["librarys"])

	#print(dir(basicModules))
	basicModules.roomSetting("settings/roominfo.json")
	# m.realModules["librarys"].RoomData.printAllObject()
	basicModules.mapSetting("3x3", 2, path="settings/")
	# m.realModules["librarys"].MapData.printMaptable()
	basicModules.mobSetting(path = "settings/monsters.json")
	# m.realModules["librarys"].MobData.printAllObject()
	basicModules.charSetting(path ="settings/characters.json")
	# m.realModules["librarys"].CharData.printAllObject()
	basicModules.itemSetting(path = "settings/items.json")
	# m.realModules["librarys"].ItemData.printAllObject()
	basicModules.textSetting(path = "settings/texts.json")

	basicModules.skillSetting(path = "settings/skills.json")

	# print(basicModules.RoomData.getObjtoName(basicModules.RoomData.getNameis("")))
	
	# 방정보에서 몬스터 이름 get 후, library 에서 몬스터 생성후 저장 하고(방에 있는 몬스터 수만큼)
	data["monster"] = lib.monster.monster
	# 여기에다가 저장.(클래스형식 + 클래스 초기화)
	data["rooms"] = m.realModules["librarys"].RoomData.name
	data["monsters"] = m.realModules["librarys"].MobData.name
	data["skills"] = m.realModules["librarys"].SkillData.name
	data["characters"] = m.realModules["librarys"].CharData.name
	data["texts"] = m.realModules["librarys"].TextData.jsonData

	#print("bd", data)

	#print(m.realModules["librarys"].RoomData.number)
	#print(m.realModules["librarys"].)
	num = 3
	while True:
		num-=1
	#basicModules.twitter.get()
		retInputData = testTwit(data["players"].keys())
#		print(retInputData)
		print("\n")
		for i in data["players"]:
			if i not in retInputData:
				continue
			# print(basicModules.RoomData.getNameis(data["characters"][i]))
			#print(data["characters"])
			characterData = data["characters"][i]
			#[data["characters"][x] for x in data["characters"] if x == data["players"][i]["character"]]
			
			if data["players"][i]["flag_battle"]:
				# basicModules.ItemData.lib.saveFile("./","save.json",
				# tmp = {
				# 	"player"	:	i,
				# 	"characters":	characterData,
				# 	"rooms"		:	data["rooms"],
				# 	"texts"		:	data["texts"],
				# 	"monsters"	:	data["monsters"],
				# 	"skills"	:	data["skills"],
				# 	"inputs"	:	retInputData[i],
				# 	"monster"	:	data["monster"]
				# }
				# print(tmp)
				# print(data["players"][i])
				options = modules.battle.main(
					basicModules,
					data["players"][i],
					{
						"player"	:	i,
						"characters":	characterData,
						"rooms"		:	data["rooms"],
						"texts"		:	data["texts"],
						"monsters"	:	data["monsters"],
						"skills"	:	data["skills"],
						"inputs"	:	retInputData[i],
						"monster"	:	data["monster"]
					})
			else:
				#print(characterData)
				# if len(characterData) < 1:
				# 	pass # not played yet
				# else:
				# 	characterData = characterData[0]

				options = modules.main.main(
					basicModules,
					data["players"][i],
					{
						"player"	:	i,
						"characters":	characterData,
						"rooms"		:	data["rooms"],
						"texts"		:	data["texts"],
						"monsters"	:	data["monsters"],
						"skills"	:	data["skills"],
						"monster"	:	data["monster"],
						"inputs"	:	retInputData[i]
					})
			if options:
				print(options)
				if "move" in options:
					data["players"][i]["location"] = options["move"]
				if "state" in options:
					pass
					print(options["state"])
				if "event" in options:
					if options["event"] == "demage":
						_demages = dice(options["demage"])[0]
						m.realModules["librarys"].CharData.setObjtoName(
							m.realModules["librarys"].CharData.getNameis(data["players"][i]["character"]), "hp", _demage)
						pass
					elif options["event"] == "battle":
						data["players"][i]["flag_battle"] = True
						data["players"][i]["monster"] = options["monster"]
					elif options["event"] == "synario":
						data["players"][i]["flag_battle"] = False

				data["players"][i]["moveEvent"] = options["moveEvent"]

		basicModules.echo()
		#wait 20sec

		# if "flag_battle" in options:
		# 	data[i]["flag_battle"] = options["flag_battle"]


if __name__ == "__main__":
	main()




