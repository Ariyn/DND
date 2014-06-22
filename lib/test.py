# -*- coding:utf-8 -*-
import echo
import dice
import monster

def checkInput(data, pinput):
	if pinput in [x["key"] for x in data]:
		return True
	else:
		return False

def main(mods, datas, options):
	print(mods)
	print(datas)
	print(options)
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

if __name__ == "__main__":
	sample = {"skills":[{"smash":3},{"block":0}],"actions":[{"move":0}],"realuser":"Goblin","values":"monster","status":{"charisma":0,"hp":10,"wisdom":0,"agillity":0,"level":1,"max_hp":10,"res_magicspell":0,"res_breath":0,"res_poison":0,"res_magicstic":0,"intelligent":0,"res_sturn":0,"res_parrelize":0,"health":0,"ac":0,"strength":0,"res_magicstaff":0,"res_death":0,"class":"monster"},"charname":"Goblin"}
	options = {
		"player":{"realuser":"YuiDevelop","charname":"horo","status":{"res_magicstic":0,"res_sturn":0,"class":"healer","res_breath":0,"res_magicspell":0,"charisma":0,"intelligent":0,"res_death":0,"res_poison":0,"res_parrelize":0,"wisdom":0,"max_hp":0,"res_magicstaff":0,"agillity":0,"hp":-13,"level":1,"health":0,"ac":0,"strength":0},"skills":[{"smash":0},{"block":0}],"actions":[{"move":0}],"values":"sun"},
		"inputs":"smash",
		"skills":{"heal":{"type":"magic","damage":-5},"poison":{"type":"poison","eff":{"res_poison":-1},"damage":1},"smash":{"type":"none","damage":3}},
		"monster":monster.monster(sample)
	}

	a = echo.echo()
	b = monster.monster(sample)
	c = b.mob

	main(a, c, options)





# {
# 	"player":{"realuser":"YuiDevelop","charname":"horo","status":{"res_magicstic":0,"res_sturn":0,"class":"healer","res_breath":0,"res_magicspell":0,"charisma":0,"intelligent":0,"res_death":0,"res_poison":0,"res_parrelize":0,"wisdom":0,"max_hp":0,"res_magicstaff":0,"agillity":0,"hp":-13,"level":1,"health":0,"ac":0,"strength":0},"skills":[{"smash":0},{"block":0}],"actions":[{"move":0}],"values":"sun"},
# 	"inputs":"smash",
# 	"skills":{"heal":{"type":"magic","damage":-5},"poison":{"type":"poison","eff":{"res_poison":-1},"damage":1},"smash":{"type":"none","damage":3}},
# 	"monster":monster.monster(sample),
# }
#플레이어 인풋이 맞는가

#플레이어 인풋에 따라 효과

#몬스터의 인풋

#몬스터의 인풋에 따라 효과

#텍스트 추가

#전투 승리(=모두 죽임), 패배(=죽음), 도망시
#return {state:"승리", "죽음", "도망"}