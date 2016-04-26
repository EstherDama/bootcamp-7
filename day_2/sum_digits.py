def sum_digits (A):
	'''
	Takes a list A, and returns
	the sum of all the digits in the
	list e.g. [10,30,45] should return
	1 + 0 + 3 + 0 + 4 + 5 = 13
	'''

	total = 0

	for i in A:
		b = str(i)
		for n in b:
			total += int(n)
	return total

#test code
print sum_digits([101,300,450])
