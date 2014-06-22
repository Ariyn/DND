

def checkInput(data, pinput):
	if pinput in [x["key"] for x in data]:
		return True
	else:
		return False

def main(mods, datas, options):
	inputCorrect = checkInput(data["moveEvent"], options["inputs"])

	print("datas",datas)

	print("monsters",[x.name for x in datas["monster"]])

	mods.addEchoText(options["player"],str(text))
	pass

#플레이어 인풋이 맞는가

#플레이어 인풋에 따라 효과

#몬스터의 인풋

#몬스터의 인풋에 따라 효과

#텍스트 추가

#전투 승리(=모두 죽임), 패배(=죽음), 도망시
#return {"state":"승리", "죽음", "도망"}

