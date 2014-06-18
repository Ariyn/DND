# -*- coding:utf-8 -*-

import lib.jsonParse
import lib.echo
from lib.dice import dice

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
	
	data["rooms"] = m.realModules["librarys"].RoomData.number


	data["characters"] = m.realModules["librarys"].CharData.name
	data["texts"] = m.realModules["librarys"].TextData.jsonData

	#print("bd", data)

	#print(m.realModules["librarys"].RoomData.number)
	#print(m.realModules["librarys"].)
	num = 3
	while num > 0:
		num-=1
	#basicModules.twitter.get()
		retInputData = testTwit(data["players"].keys())
		print("\n")
		for i in data["players"]:
			if i not in retInputData:
				continue

			#print(i)
			if data["players"][i]["flag_battle"]:
				options = modules.battle.main(
					basicModules,
					data["players"][i],
					{
						"characters":data["characters"],
						"rooms":data["rooms"],
						"texts":data["texts"],
						"inputs":retInputData[i]
					})
			else:
				options = modules.main.main(
					basicModules,
					data["players"][i],
					{
						"characters":data["characters"],
						"rooms":data["rooms"],
						"texts":data["texts"],
						"inputs":retInputData[i]
					})
			if options:
				if "move" in options:
					data["players"][i]["location"] = options["move"]
				if "state" in options:
					print(options["state"])
				if "event" in options:
					if options["event"] == "demage":
						_demages = dice(options["demage"])[0]
						m.realModules["librarys"].CharData.setObjtoName(
							m.realModules["librarys"].CharData.getNameis(data["players"][i]["character"]), "hp", _demage)
						pass
					elif options["event"] == "battle":
						data["players"][i]["flag_battle"] = True
					elif options["event"] == "synario":
						data["players"][i]["flag_battle"] = False

				data["players"][i]["moveEvent"] = options["moveEvent"]

		basicModules.echo()


		# if "flag_battle" in options:
		# 	data[i]["flag_battle"] = options["flag_battle"]


if __name__ == "__main__":
	main()




