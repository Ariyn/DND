import pdb
import codecs
import roominfo
import sys, json, re, importlib

def printu(text):
	sys.stdout.buffer.write((text+"\n").encode('utf-8'))

if __name__ == "__main__":
	a = test()
	a.main()

	