# -*- coding:utf-8 -*-

import sys, os, json, codecs, random


class echo:
	files = {}
	echoText = {}

	def addEchoFiles(self, name):
		#print(os.path.abspath("../scripts/"+name))
		try:
			f = codecs.open(os.path.abspath("../scripts/"+name), "r","utf-8")
		except FileNotFoundError:
			return False

		self.files[name[:-5]] = json.loads(f.read())

		#self.printu(self.files[name])
		return True

	def addEchoText(self, pid, text):
		print("id",pid)
		self.echoText[pid] = text

	def printu(self, text):
		sys.stdout.buffer.write((text+"\n").encode('utf-8'))

	def prinutTest(self, *text):
		text = ''.join(str(text))
		sys.stdout.buffer.write((str(text)+"\n").encode('utf-8'))

	# def echo(self, _target = "", _type = "", _index = -1):

	# 	if _target in self.files and _type in self.files[_target]:
	# 		if _index == -1:
	# 			self.printu(random.choice(self.files[_target][_type]))
	# 		else:
	# 			self.printu(self.files[_target][_type][_index])
	# 	elif _target not in self.files:
	# 		return "target"
	# 	elif _type not in self.files[_target]:
	# 		return "type"
	def echo(self, _text = ""):

		for i in self.echoText:
			print(self.echoText[i]+"\n")
		self.echoText = {}

	def Message(self):
		rt = []
		tmp = self.echoText
		for key in tmp:			
			ha = {}
			ha["id"] = key
			ha["text"] = tmp[key]
			rt.append(ha)
		return rt


if __name__ == "__main__":
	t = echo()