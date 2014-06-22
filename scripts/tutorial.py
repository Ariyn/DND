

def checkProgress(datas, options):
	if "flag_name" in datas and datas["flag_name"]:
		return "flag_name"
	elif "flag_class" in datas and datas["flag_class"]:
		return "flag_class"
	elif "flag_status" in datas and datas["flag_status"]:
		return "flag_status"
	elif "flag_newbie" in datas and datas["flag_newbie"]:
		return "flag_newbie"

def main(mods, datas, options):
	if datas["flag_newbie"]:
		progress = checkProgress(datas, options)
	else:
		return None

	print(progress)
	print(datas)
	retData = {}
	if progress == "flag_newbie":
		
		mods.addEchoText(options["player"],"오오, 우리를 구원하실 용사님이시군요. \n용사님이 오시기 만들 손꼽아 기다리고 있었습니다. 산 아래 트롤들이 너무나 강력해 저희로써는 도저히 손을 쓸 수가 없었습니다. 그런데 용사님의 존함이 무엇인지 여쭤봐도 되겠습니까?")

		mods.addEchoText(options["player"],"- 주의 -\n캐릭터의 이름은 알파벳, 숫자, 한글, 일본어, 중국어를 섞어서 6자 이내로 등록해주시기 바랍니다.")

		datas["flag_name"] = True
		#datas["flag_newbie"] = False

	elif progress == "flag_name":
		print(options["inputs"])
		if len(options["inputs"]) > 6:
			return None
		else:
			datas["character"] = options["inputs"]
			datas["flag_class"], datas["flag_name"] = True, False

		mods.addEchoText(options["player"],str(datas["character"])+" 용사님 이시군요! 신이시여,감사합니다!\n저희의 마을이 이렇게 황폐하지만 않았어도 용사님께 귀한 대접을 해드렸을텐데, 산 아래 트롤때문에 드릴 수 있는게 없군요. 그런데 용사님의 직업은 무엇인가요?")

		mods.addEchoText(options["player"],"- 주의 -\n캐릭터의 직업은 알파벳, 숫자, 한글, 일본어, 중국어를 사용해서 띄어쓰기 없이 6자 이내로 등록해주시기 바랍니다.")

	elif progress == "flag_class":
		print(options["inputs"])
		if len(options["inputs"]) >= 6:
			return None
		else:
			datas["class"] = options["inputs"]
			datas["flag_status"], datas["flag_class"] = True, False
			datas["moveEvent"] = ["#능력"]

		mods.addEchoText(options["player"],"세상에! "+str(datas["class"])+" 라는 직업도 있었군요. 밥은 먹고 다니시나요?")
		mods.addEchoText(options["player"],"흠! 흠! 죄송합니다. 제가 용사님께 실례를 범했군요. 그만 마음속 소리가.. 어찌됬건 용사님, 저희가 용사님의 능력을 좀 볼 수 있을까요?")
		mods.addEchoText(options["player"],"- 알림 -\n캐릭터의 스텟(능력치)는 #능력치 라고 입력하면 볼 수 있습니다.")

	elif progress == "flag_status" and options["inputs"] in datas["moveEvent"]:
		
		options["characterM"].setBasicChar(datas["character"],options["player"],"착함",datas["class"])
		print(options["player"],options["characterM"].name)
		#{"character":"miko","synario":"기본","location":83,"flag_battle":False,"flag_newbie":False,"moveEvent":[]}
		datas["flag_battle"] = False
		datas["synario"] = True
		datas["location"] = 0
		datas["moveEvent"] = []

		mods.addEchoText(options["player"],datas["character"]+"\n"+str(
			options["characterM"].name[options["player"]]))

		mods.addEchoText(options["player"],"오 이정도면! 우리가 찾던 그 용사님이 맞는것 같습니다. 자 이제! 빨리 여행을 떠나 주세요!. 한시라도 급합니다. 산아래 있는 동굴까지는 저희가 안내해 드리도록 하겠습니다. 그럼 행운을!")

		datas["flag_newbie"] = False



