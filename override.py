

class plist(list):
	def append(self, i):
		print(i)
		pass

list = plist

a = [10,20,30,40,50]

a.append(70)