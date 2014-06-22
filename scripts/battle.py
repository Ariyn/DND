# -*- coding:utf-8 -*-
import dice

def checkInput(data, pinput):
	if pinput in [x["key"] for x in data]:
		return True
	else:
		return False

def main(mods, datas, options):
	print("input: " + options["inputs"])
	# datas["location"]#사용자 위치고
	# options["rooms"]#사용자 위치랑 같은 방이름 찾고 거ㅣ있는 몬스터 이름을 겟
	# options["monsters"] #가져온 몬스터이름이랑 같은 애ㅑ를 리턴
	# print(datas["location"])
	monsters = []
	# print(options["monsters"])
	for key in options["rooms"]:
		# print(key)
		if str(datas["location"]) == str(key):
			mname = options["rooms"][key]["monsters"]
			monsters.append(options["monsters"][mname[0]])
			break

	# print(options["characters"])
	# print(options["rooms"])
	# print(datas)
	# for i in datas["moveEvent"]:
	# 	for key in i:
	# 		print(key)
	# 		if key == "도망친다":
	# 			print("도망!!!!!!!!!")
	inputCorrect = checkInput(datas["moveEvent"], options["inputs"])

	if datas["moveEvent"] == "도망친다":
		result["state"] = "도망"
		text = text + "도망칩니다.\n"
		mods.addEchoText(options["player"],str(result))
		print("escape!!!!!")
		return result

	result = {}
	result["moveEvent"] = ""
	skills = options["skills"]

	character = options["characters"]
	# print("chars: ")
	# print(character)
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
	# monsters = options["monster"].mob
	# print("mob: ")
	# print(monsters)
	for monster in monsters:
		if monster["status"]["hp"] <= userskill_damage:
			monster["status"]["hp"] = monster["status"]["hp"] - userskill_damage	
			text = text + monster["realuser"] + "에게 " + str(monster["status"]["hp"]) +"의 대미지를 입혔다." + "남은 hp = 0 \n"
			if monster["status"]["hp"] != 0:
				userskill_damage = userskill_damage % monster["status"]["hp"]
			text = text + monster["realuser"] + "이(가) 죽었다.\n"
			mods.addEchoText(options["player"],str(text))
			if monster["status"]["hp"] <= 0:
				if monsters[len(monsters)-1] == monster:
					result["state"] = "승리"
					text = text + "승리했습니다.\n"
					mods.addEchoText(options["player"],str(text))
					return result
				continue
			continue
		else:
			monster["status"]["hp"] = monster["status"]["hp"] - userskill_damage
			text = text + monster["realuser"] + "에게 " + str(userskill_damage) +"의 대미지를 입혔다." + "남은 hp = " + str(monster["status"]["hp"]) + "\n"
			mods.addEchoText(options["player"],str(text))
		mobskill_name = "smash"
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
			text = text + monster["realuser"] + "이(가) " + str(mobskill_damage) +"의 대미지를 입었다." + "남은 hp = " + str(character["status"]["hp"]) + "\n"
			mods.addEchoText(options["player"],str(text))
			if character["status"]["hp"] <= 0 :
				result["state"] = "사망"
				text = text + "죽었습니다.\n"
				mods.addEchoText(options["player"],str(text))
				return result

	
		
	result["moveEvent"] = datas["moveEvent"]
	return result

if __name__ == "__main__":
	pass

#플레이어 인풋이 맞는가

#플레이어 인풋에 따라 효과

#몬스터의 인풋

#몬스터의 인풋에 따라 효과

#텍스트 추가

#전투 승리(=모두 죽임), 패배(=죽음), 도망시
#return {state:"승리", "죽음", "도망"}