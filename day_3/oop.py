#classes
#PEP8 stardands on how to write python case
#Data(properties) and behaviour

class Person:
	#class variable
	people_count = 0

	def __init__(self, name, age) : 
		self.name = name
		self.age = age
		Person.people_count += 1

	def say_hello(self):
		return "Hello, I'm {} and {} y/o" .format(self.name, self.age)

	def  __repr__(self): #special function that gives a good formated representation of an object
		return "<object: {}, {}>".format(self.name,self.age)


p = Person('Joe', 23)
p2 = Person('Jane', 23)
p3 = Person('George', 40)


print p2.people_count # will refer to people class for this value 

a = [('Jane', 23), ('Joe', 50), ('Jackie', 34), ('Jacob', 23), ('Jee', 18), ('Josh', 60)] 

b = []

for name,age in a: 
	person = Person(name, age)
	b.append(person)

print Person.people_count
# print  b

# print p.say_hello()

for item in b: 
	print item.say_hello() 