import d40lib, json, sys, codecs
import dice

class Skills:

	def __init__(self, path = "../settings/skills.json"):
		try:
			self.file = codecs.open(path,"r","utf-8")
		except FileNotFoundError as err:
			print(err)
			return None


		self.jsonData = self.file.read()
		try:
			self.data = json.loads(self.jsonData)
		except ValueError as err:
			print(err)
			return None

	def appendChar(self, data):
		self.character = data

	def parseData(self, character, data):
		spliText = data.split(" ")
		pass

	def getData(self, name):
		if name in [x["name"] for x in self.data]:
			ind = [x["name"] for x in self.data].index(name)
			return self.data[ind]
		else:
			return None

def main():
	s = skill()
	sys.stdout.buffer.write(str(s.getData("파이어볼")).encode("utf-8"))

if __name__ == "__main__":
	main()