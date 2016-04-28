def super_sum(*args):
	'''
	Returns the sum of numbers.

	e.g 
		super_sum () ==> "Please Enter numbers"
		super_sum (1, 2, 3) ==> 6
		super_sum ([1, 2, 3]) ==> 6
		super_sum ([10], [20, 30]) ==> 60
	'''
	if not args:
		return "Please Enter numbers"