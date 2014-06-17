# -*- coding:utf-8 -*-

import lib.jsonParse
import lib.echo
import parse_nature

def testTwit():
	return input()
def main():
	m = parse_nature.oModules()
		#data = bModules()
		
	data = {
		"players":
		{
			"YuiDevelop":{"synario":"기본","location":0,"flag_battle":False},
			"MuTopia_ArtTeam":{"synario":"기본","location":0,"flag_battle":False},
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
	#while True:
	#basicModules.twitter.get()
	retData = testTwit()

	for i in data["players"]:
		#print(i)
		options = modules.main.main(
			basicModules,
			data["players"][i],
			{
				"characters":data["characters"],
				"rooms":data["rooms"],
				"texts":data["texts"]
			})

	basicModules.echo()


		# if "flag_battle" in options:
		# 	data[i]["flag_battle"] = options["flag_battle"]


if __name__ == "__main__":
	main()




