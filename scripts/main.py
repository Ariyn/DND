#main.py
# -*- coding:utf-8 -*-

#returns must like this
#status, data, options

def main(mods, data, options):
	retData = {
		"moveEvent":[],
	}

	playerSynarioNum = data["location"]
	gameData = [x for x in options["texts"] if x["number"] == playerSynarioNum][0]
	moveEvents = gameData["moveEvent"]

	text = gameData["text"]
	for i in moveEvents:
		text += "\n"+i
		retData["moveEvent"].append({"key":i,"target":moveEvents[i]})

	mods.addEchoText(str(text))
	return retData