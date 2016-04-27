from person import Person #from the person file import the class Person  
from kenyan import Kenyan
#classes
#PEP8 stardands on how to write python case
#Data(properties) and behaviour
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


#Kenyan things for inheritance

k = Kenyan('Miguna', 20)

k.probe(True)

print "Is {} corrupt? {}".format( k.name, k.is_corrupt())

print k.say_hello()