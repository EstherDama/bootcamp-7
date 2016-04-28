def string_length(elements):
  b = []

  if type(elements) == str:
    b.append(len(elements))
    return b
    
  elif type(elements) == list:
    for element in elements:
      b.append(len(element))
  return b

print string_length("Godson")
print string_length(["Godson", "Joy"])
print string_length(["Godson", "Joy", "Rank"])