def funky(a,b):

    if type(a) == str and type(b) == str:
        return a + b

    elif type(a) == int and type(b) == int:
        return a + b

    elif type(a) == float and type(b) == float:
        return a + b

    elif type(a) == list and type(b) == list:
        return a + b

    elif type(a) == dict and type(b) == dict:
    	return ("This is a dictionary!!! What do you expect me to do?")

    else:
        return ("Error")

print funky("uptown","funk")
print funky(6,8)
print funky(4.8, 3.3)
print funky([34,45,56,67],[25,53,36,67])
print funky("uptown", 8)
print funky(4.9, 8)

a = {"artist": "mark ronson","song": "uptown funk"}
b = {"featuring":"bruno mars", "year": 2015}
print funky(a,b)