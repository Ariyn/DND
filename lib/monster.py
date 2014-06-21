import codecs

class monster:
	name, level, status = "", 0, {}
	skills, actions = {}, {}

	def __init__(self, data):
		if len(data) == 1:
			#print(data[0])
			self.name = data[0]["charname"]
			self.level = data[0]["status"]["level"]
			self.status = data[0]["status"]
			self.skills = data[0]["skills"]
			self.actions = data[0]["actions"]

			print(self.name)
			print(self.level)
			print(self.status)
			print(self.skills)
			print(self.actions)
		else:
			pass#error

	def nextAction(self):
		return "basic"

if __name__ == "__main__":
	mons = [monster(), monster()]

	mons[0].level = 2

	print(mons[0].level)
	print(mons[1].level)