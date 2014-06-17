#main.py
# -*- coding:utf-8 -*-

#returns must like this
#status, data, options

def checkInput(data, pinput):
	if pinput in [x["key"] for x in data]:
		return True
	else:
		return False

def main(mods, data, options):
	inputCorrect = checkInput(data["moveEvent"], options["inputs"])
	retData = {
		"moveEvent":[],
	}
	playerSynarioNum = data["location"]

	if inputCorrect:
		gameData = [x for x in options["texts"] if x["number"] == playerSynarioNum][0]
		playerSynarioNum = gameData["moveEvent"][options["inputs"]]
		
		retData["move"] = playerSynarioNum

	
	gameData = [x for x in options["texts"] if x["number"] == playerSynarioNum][0]
	moveEvents = gameData["moveEvent"]

	text = gameData["text"]
	for i in moveEvents:
		text += "\n"+i
		retData["moveEvent"].append({"key":i,"target":moveEvents[i]})

	mods.addEchoText(str(text))
	return retData