import TwitterEngine
import codecs,sys
import json
import time
import dice
import threading
import librarys

def printu(text):
	sys.stdout.buffer.write((text+"\n").encode('utf-8'))

if __name__ == "__main__":
	lib = librarys.librarys()
	twit = librarys.TwitterForm()
	# init
	# lib.mobSetting()
	# # get monster
	# monsters = lib.MobData
	# # monsters.printAllObject()
	# monsters.setObjtoName(monsters.getNameis("a"), "charname", "goblin")
	# # monsters.setBasicChar("Goblin", "Goblin", "monster", "monster")
	# # monsters.saveFile(monsters._path,"")
	# monsters.printAllObject()







# battle

	# sample battle system
	# -- skill setting --
	lib.skillSetting()
	# -- char setting --
	lib.charSetting()
	# -- mob setting --
	lib.mobSetting()
	# 
	chars = lib.CharData
	skills = lib.SkillData
	mobs = lib.MobData
	# print
	# print("skill name : effect")
	# skills.printAllObject()
	# print("charname : informations")
	# chars.printAllObject()
	# print("mobname : informations")
	# mobs.printAllObject()
	# sample battle
	# get user information "yuidev"
	mobskills = mobs.getObjtoName(mobs.getNameis("Goblin"),"skills")
	mobskill_name = ""
	mobskill_eff = ""
	mobskill_damage = 0
	mobskill_type = ""
# $ methods ------------------------------------------------------------------------------
	for skill in mobskills:
		print(skill)
		for key in skill:
			print(key)
			if (skill[key] != 0):
				f = dice.dice("1d"+str(skill[key]))[0]
				mobskill_name = key
				mobskill_damage = skills.getObjtoName(skills.getNameis(mobskill_name), "damage") - f
				mobskill_type = skills.getObjtoName(skills.getNameis(mobskill_name), "type")
				mobskill_eff = skills.getObjtoName(skills.getNameis(mobskill_name), "eff")
			
# ----------------------------------------------------------------------------------------
	if (mobskill_name is None) :
		print("missed attack")
	else:
		print("Goblin's battle!!")
		print("Goblis is use the " + mobskill_name + "!!")
		print("attacked Goblin!! U damaged " +str(mobskill_damage) + "!!")
		chars.setObjtoName(chars.getNameis("yuidev"), "hp", -(mobskill_damage))
		chars.saveFile(chars._path,"")
		
	print("You're Status -")
	print(chars.getNameis("yuidev"))
