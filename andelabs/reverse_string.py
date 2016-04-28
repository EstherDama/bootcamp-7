def reverse_string(input):
  
  reversed = input[::-1]
  # reversed = the_reversal(input)
  if  input == "":
    return None
  elif reversed == list(input):
    return True
  else:
    return reversed

#You can define a function where you put the word to be reversed or us the operator above
# def the_reversal(string):

#   b = []

#   for item in range(len(string)-1, -1, -1):
#     b.append(string[item])
#     str1 = "".join(b)
#   return b


print reverse_string("civic")
print reverse_string("books")