# -*- coding:utf-8 -*-

import dice

def checkInput(data, pinput):
	if pinput in [x["key"] for x in data]:
		return True
	else:
		return False

def main(mods, datas, options):
	if datas["moveEvent"] == "도망간다":
		result["state"] = "도망"
		mods.addEchoText(options["player"],str(result))
		print("escape!!!!!")
		return result

	inputCorrect = checkInput(datas["moveEvent"], options["inputs"])
	result = {}
	result["moveEvent"] = ""
	skills = options["skills"]

	character = datas["character"]
	if inputCorrect:
		userskill_name = options["inputs"]
	else:
		userskill_name = "smash"
	userskill_eff = ""
	userskill_damage = 0
	userskill_type = ""
	f = dice.dice("1d"+str(skills[userskill_name]["damage"]))[0]
	userskill_damage = skills[userskill_name]["damage"] - f
	userskill_type = skills[userskill_name]["type"]

	text = ""
	monsters = options["monster"].mob
	for monster in monsters:
		if monster["status"]["hp"] < userskill_damage:
			userskill_damage = userskill_damage % monster["status"]["hp"]
			options.remove(monster)
			text = text + monster["realname"] + "에게 " + userskill_damage +"의 대미지를 입혔다.\n" + "남은 hp = " + monster["status"]["hp"] + "\n"
			text = text + monster["realname"] + "이(가) 죽었다.\n"
			continue
		else:
			monster["status"]["hp"] = monster["status"]["hp"] - userskill_damage
			text = text + monster["realname"] + "에게 " + userskill_damage +"의 대미지를 입혔다.\n" + "남은 hp = " + monster["status"]["hp"] + "\n"
		mobskill_name = montser.nextAction()
		mobskill_eff = ""
		mobskill_damage = 0
		mobskill_type = ""

		f = dice.dice("1d"+str(skills[mobskill_name]["damage"]))[0]
		mobskill_damage = skills[mobskill_name]["damage"] - f
		mobskill_type = skills[mobskill_name]["type"]

		if (mobskill_name is None) :
			pass
		else:
			character["status"]["hp"] = character["status"]["hp"] - mobskill_damage
			text = text + monster["realname"] + "이(가) " + mobskill_damage +"의 대미지를 입혔다.\n" + "남은 hp = " + character["status"]["hp"] + "\n"

	if len(monsters) == 0:
		result["state"] = "승리"
		mods.addEchoText(options["player"],str(text))
		return result

	if character["status"]["hp"] <= 0 :
		result["state"] = "사망"
		mods.addEchoText(options["player"],str(text))
		return result
		
	result["moveEvent"] = datas["moveEvent"]
	return result


#플레이어 인풋이 맞는가

#플레이어 인풋에 따라 효과

#몬스터의 인풋

#몬스터의 인풋에 따라 효과

#텍스트 추가

#전투 승리(=모두 죽임), 패배(=죽음), 도망시

#return {state:"승리", "죽음", "도망"}
