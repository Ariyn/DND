

def checkProgress(datas, options):
	if "flag_newbie" in datas and datas["flag_newbie"]:
		return "flag_newbie"
	elif "flag_name" in datas and datas["flag_name"]:
		return "flag_name"
	elif "flag_class" in datas and datas["flag_class"]:
		return "flag_class"
	elif "flag_status" in datas and datas["flag_status"]:
		return "flag_status"

def main(mods, datas, options):
	print("here")
	if datas["flag_newbie"]:
		progress = checkProgress(datas, options)
	else:
		return None

	retData = {}
	if progress == "flag_newbie":
		mods.addEchoText(options["player"],"오오, 우리를 구원하실 용사님이시군요. \n용사님이 오시기 만들 손꼽아 기다리고 있었습니다. 산 아래 트롤들이 너무나 강력해 저희로써는 도저히 손을 쓸 수가 없었습니다. 그런데 용사님의 존함이 무엇인지 여쭤봐도 되겠습니까?")

		mods.addEchoText(options["player"],"- 주의 -\n캐릭터의 이름은 알파벳, 숫자, 한글, 일본어, 중국어를 섞어서 6자 이내로 등록해주시기 바랍니다.")

	elif progress == "flag_name":
		print(options["inputs"])
		if len(options["inputs"]) >= 6:
			return None
		mods.addEchoText(options["player"],options["inputs"]+" 용사님 이시군요! 신이시여! 감사합니다! 저희의 마을이 이렇게 황폐하지만 않았어도, 용사님께 귀한 대접을 해드렸을텐데, 산 아래 트롤때문에 드릴 수 있는게 없군요. 그런데 죄송하지만 용사님의 직업 어떻게 되십니까?")

		
