import TwitterEngine
import codecs,sys
import json
import time
import threading

def printu(text):
	sys.stdout.buffer.write((text+"\n").encode('utf-8'))

if __name__ == "__main__":
	a = []
	b = {"":""}
	for i in range(2):
		a.append(b)
	print(a)
	# a = DND_twitter()