class Person(object): # if you dont inherite from object i cannot have basic python object characteristics. So it cannot inherit
	#class variable
	people_count = 0

	def __init__(self, name, age = 0) : 
		self.name = name
		self.age = age
		Person.people_count += 1

	def say_hello(self):
		return "Hello, I'm {} and {} y/o" .format(self.name, self.age)

	def  __repr__(self): #special function that gives a good formated representation of an object
		return "<object: {}, {}>".format(self.name,self.age)