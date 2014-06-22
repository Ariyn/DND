import TwitterEngine
import codecs,sys
import json
import time
import threading
import librarys

def printu(text):
	sys.stdout.buffer.write((text+"\n").encode('utf-8'))

if __name__ == "__main__":
	lib = librarys.librarys()
	twit = librarys.TwitterForm()
	# init
	lib.mobSetting()
	# get monster
	monsters = lib.MobData
	# monsters.printAllObject()
	monsters.setObjtoName(monsters.getNameis("a"), "charname", "goblin")
	# monsters.setBasicChar("Goblin", "Goblin", "monster", "monster")
	# monsters.saveFile(monsters._path,"")
	monsters.printAllObject()