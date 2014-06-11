#main.py
# -*- coding:utf-8 -*-

#returns must like this
#status, data, options

def init(mods):
	e = mods.addEchoFiles("ariyn.json")
	#print(e)

def main(mods, data, options = None):
	#print(data.player.synario)
	init(mods)
	mods.echo("ariyn", data["player"]["synario"], data["player"]["script"])