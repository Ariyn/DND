
import random, math


def dice(typeText):
	spliText = typeText.split("d")
	# print(spliText)
	dices = []

	if spliText[0] == "" and spliText[1] == "%":
		dices.append(math.floor(((random.random()*10)%10+1)*10 +(random.random()*10)%10))
	elif len(spliText) == 2:
		dieFace, diceNumber = int(spliText[1]), int(spliText[0])

		for i in range(diceNumber):
			dices.append(math.floor((random.random()*100)%dieFace+1))
	return dices


if __name__ == "__main__":
	print(dice("20d3"))
