
# def words(word):
# 	for c in word:
# 		if c.isspace():
# 			string_list = word.split()

# 	string_dict = {}

# 	for word in string_list:
# 		if word in string_dict:
# 			string_dict[word] = string_dict[word] + 1
# 		else:
# 			string_dict[word] = 1
# 	return string_dict

string = "olly olly in come come free"
print words(string)
print words('go Go GO')
# words('¡Hola! ¿Qué tal? Привет!')
# dict = word_count(string)
# print(dict)

#the one that works with one error
def words(word):
	string_list = word.split()
	string_dict = {}

	for word in string_list:
		if word in string_dict:
			string_dict[word] = string_dict[word] + 1
			continue
		else:
			string_dict[word] = 1
	return string_dict