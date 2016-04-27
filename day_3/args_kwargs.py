#Unpacking
def hello(name, age, class_ = ''):
	'''
	Explains....
	'''
	if class_ != '':
		return "I am {}, {}y/o, and {} class".format(name,age, class_)
	return "I am {}, and I'm {}".format(name, age)

people = [("Jane", 23, 'High'), 
			("Joe", 25, 'Low'),
			("Brian", 60),
			("Betty", 45)
			]

#for unpacking
for i in people:
	print hello(*i)

#another way of doing this
#for name,age in people:
	#print hello(name,age)

#and yet another way
#for i in people:
	#print hello(i[0],i[1])
