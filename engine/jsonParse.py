# -*- coding:utf-8 -*-

import json, importlib, os.path

class jsonC:
	def __init__(self, path = "./sample.json", pathType = "r"):
		self.file = open(path, pathType)
		self.jsonData = json.loads(self.file.read())

def xfile(afile, globalz=None, localz=None):
    with open(afile, "r") as fh:
        exec(fh.read(), globalz, localz)



def main():
	path = "../settings/"
	filename = "sample_event.json"

	check = jsonC(path+filename)
	#print(check.jsonData)

	################################################################
	modules = []

	realPath = os.path.abspath(path)+"/"
	print(path+check.jsonData["event"])
	print(realPath)

	namespace = {}
	xfile(realPath+"/"+check.jsonData["event"]+".py",namespace)
	
	globals().update(namespace)
	all_names = namespace.get("__all__")

if __name__ == "__main__":
	main()