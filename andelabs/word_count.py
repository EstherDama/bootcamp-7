def words(string):
  new_list = string.split()
  string_dict = {}

  for word in new_list:
    if word.isdigit(): 
      word = int(word)

    if word in string_dict:
      string_dict[word] +=  1
      
    else:
      string_dict[word] = 1
  return string_dict



print words("Hi hi hi how are : : yah")
string = "olly olly in come come free"
print words(string)
print words('go Go GO')
