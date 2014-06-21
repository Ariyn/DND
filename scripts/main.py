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
		"moveEvent":[],"state":[]
	}
	playerSynarioNum = data["location"]

	if inputCorrect:
		gameData = [x for x in options["texts"] if x["number"] == playerSynarioNum][0]
		playerSynarioNum = gameData["moveEvent"][options["inputs"]]
		
		retData["move"] = playerSynarioNum
	
	gameData = [x for x in options["texts"] if x["number"] == playerSynarioNum][0]
	if "moveEvent" in gameData:
		moveEvents = gameData["moveEvent"]
	if "event" in gameData:
		events = gameData["event"].split(" ")

		if events[0] == "battle":
			retData["event"] = events[0]
			retData["eventTarget"] = events[1]
			if events[1] == "monster":
				retData["monster"] = gameData["monster"]
				print(retData["monster"])
			elif events[1] == "playerName":#not yet!
				pass

		elif events[0] == "demage":
			retData["event"] = events[0]	
			retData["eventTarget"] = events[1]
			retData["demage"] = events[2]
			

	text = gameData["text"]
	for i in moveEvents:
		splitText= i.split(" ")
		if len(splitText) == 2 and splitText[0] == "state":
			retData["state"].append(splitText[1])
			continue
		text += "\n"+i
		retData["moveEvent"].append({"key":i,"target":moveEvents[i]})
	if "event" in gameData and retData["event"] == "battle":
		for i in options["characters"]["skills"]:
				retData["moveEvent"].append({"key":i,"target":None})
				text += "\n"+i
		
	mods.addEchoText(str(text))
	return retData