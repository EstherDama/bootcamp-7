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

#overloading of parameters in Java
#changes to a list the * arguements
def super_sum(a, b, *args):
	'''
	Takes in variable number of items,
	and returns the sum.
	e.g. super_sum(10, 20) = 30
		 super_sum(10, 20, 40) = 70
		 super_sum (1, 4, 5, 6, 7) = 23
	'''
	total = 0

	for i in args :
		total += i
	return total + a + b

print super_sum(10,20)
print super_sum(1, 4, 5, 7)
a = [10, 40, 60]
print super_sum(*a)  





#now for kwargs
#changes the list of parameters to dictonary
# To unpack a dictonary **
def hello_again (**kwargs): 
	return "I am {}, and I'm {}". format(kwargs['name'], kwargs['age'])

#test the kwargs
print hello_again(name='Joe', age=20)
print hello_again(age=20, name='Jane')

other_people = [
				{'name':'Joe', 'age': 98},
				{'name':'Jane', 'age': 60},
				{'name':'Trump', 'age': 23}
				]

joe = {'name':'Joe', 'age': 98}

print hello_again(**joe) #this is the same as the line below
print hello_again(name = 'Joe', age = 98)

for person in other_people:
	print hello_again(**person)