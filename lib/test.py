import pdb
import codecs
import roominfo
import sys, json, re

def printu(text):
	sys.stdout.buffer.write((text+"\n").encode('utf-8'))

if __name__ == "__main__":
	a = roominfo.SetRoom("./roominfo.json")
	a.setAuto()
	a.printAllObject()
	