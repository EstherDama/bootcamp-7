def data_type(x):
	'''
	Takes in an arguement, x:
		-For an integer, returns x**2
		-For a float, return x /2
		-For a string, returns "hello" + x
		-For a Boolean, return "boolean"
		-For a long, return squareroot(x)
		(4**0.5)
		or import math
		math.sqrt(x)
	'''
	if type(x) == int:
		return x ** 2
	
	elif type(x) == float:
		return x /2

	elif type(x) == str:
		return "Hello {}".format(x)

	elif type(x) == bool:
		return "boolean"

	elif type(x) == long:
		return "long"

	else:
		return "Please Enter a Valid Input"

#testing
print data_type(5)
print data_type(0.5)
print data_type("Esther")
print data_type(True)
print data_type(51924361L)
print data_type([34,56,89])