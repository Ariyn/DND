# -*- coding:utf-8 -*-

import sys, os, json, codecs, random

class echo:
	files, echoText = {}, {}
	tf = None

	debug = True
	def echoTwitterSetting(self, twit):
		self.tf = twit

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
		
		if pid not in self.echoText:
			self.echoText[pid] = []

		self.echoText[pid].append(text)


	def printu(self, text):
		sys.stdout.buffer.write((text+"\n").encode('utf-8'))

	def prinutTest(self, *text):
		text = ''.join(str(text))
		sys.stdout.buffer.write((str(text)+"\n").encode('utf-8'))

	def echo(self, debug = True):
		if debug:
			for i in self.echoText:
				print(str([x for x in self.echoText[i]])+"\n")
		else:
			# for i in self.echoText:
			# 	print(str([x for x in self.echoText[i]])+"\n")
			self.tf.sendMessages(self.Message())
			self.echoText = {}


	def Message(self):
		rt = []
		tmp = self.echoText
		for key in tmp:
			for text in reversed(tmp[key]):
				ha = {}
				ha["id"] = key
				ha["text"] = text
				rt.append(ha)
		return rt


if __name__ == "__main__":
	t = echo()

	lis = [{"test":"ss"},{"test":"ss"},{"test":"ss"}]

	for i in lis:
		print(i.keys()[0])

	#t.echo(False)