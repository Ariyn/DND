import codecs
import dice

class monster:
	name, level, status = "", 0, {}
	skills, actions = {}, {}
	mob = []

	def __init__(self, data):
		if len(data) != 0:
			#print(data[0])
			self.mob.append(data)
			self.name = data["charname"]
			self.level = data["status"]["level"]
			self.status = data["status"]
			self.skills = data["skills"]
			self.actions = data["actions"]
		else:
			pass#error

	def nextAction(self):
		rt = None
		use = False
		basePer = 70
		for skill in self.skills:
			if (dice.dice("d%")[0] <= basePer) and (use is False):
				for name in skill:
					rt = name
				basePer -= 10
				use = True
		if (rt is None):
			rt = self.nextAction()

		return str(rt)

if __name__ == "__main__":
	data = {"skills":[{"smash":3},{"block":0}],"actions":[{"move":0}],"realuser":"Goblin","values":"monster","status":{"charisma":0,"hp":10,"wisdom":0,"agillity":0,"level":1,"max_hp":10,"res_magicspell":0,"res_breath":0,"res_poison":0,"res_magicstic":0,"intelligent":0,"res_sturn":0,"res_parrelize":0,"health":0,"ac":0,"strength":0,"res_magicstaff":0,"res_death":0,"class":"monster"},"charname":"Goblin"}
	mons = monster(data)

	test = mons.nextAction()
	print(mons.name)
	print(test)

	# mons[0].level = 2

	# print(mons[0].level)
	# print(mons[1].level)