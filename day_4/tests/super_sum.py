def super_sum(*args):
	'''
	Returns the sum of numbers.

	e.g 
		super_sum () ==> "Please Enter Inputs"
		super_sum("string") ==> 0
		super_sum (1, 2, 3) ==> 6
		super_sum ([1, 2, 3]) ==> 6
		super_sum ([10], [20, 30]) ==> 60
	'''
	
	total = 0

	if not args:
		return 0

	else:

		for x in args:
			if type(x) == list:
				total += sum(x)
			elif type(x) == str:
				return 0
			else:
				total += x
		return total

#another way of doing it
		# for x in args:
		# 	if type(x) == int:
		# 		total = total + x
		# 	elif type(x) == list:
		# 		for i in x:
		# 			total += i
		# return total