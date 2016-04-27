def assignment (*args):
	for i in args: 
		return "{}: {}, ".format(label, value)

#assignment again
f = [(10, 20, 30), (10, 40) , (4, 5, 20)] 

'''
x: 10, y: 20, z: 40
x: 10, y: 40
...
'''
#l = [x, y, z]

for item in f:
	#length = len(item)
	#b = str(item)
	for n in item: 
		print assignment('x',n)
	print (''),