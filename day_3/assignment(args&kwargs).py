#joy
# def vary_loops(*args):
#     # args here are ([(10,20,40), (23,45), (23,45,67)])

#     for item in args:
#         # item here is [(10,20,40), (23,45), (23,45,67)]
#         # len(item) here is 3.
#         # So we'll execute the 'elif len(item) == 3' block

#         if len(item) == 1:  # Not true, doesn't execute.
#             for x in item:
#                 return "x: {}".format(x)
#         elif len(item) == 2:  # Not true, doesn't execute.
#             for x, y in item:
#                 return "x: {}, y:{}".format(x, y)

#         # True, so we execute.
#         elif len(item) == 3:
#             for x, y, z in item:
#                 # In here, x = (10, 20, 40), y = (23, 45), z = (23, 45,76).
#                 # By good luck, the first element has 3 elements, so the return statement passes.
#                 # If it had two, it would fail since it's expecting to see 3 elements, x, y and z.

#                 # If you were to replace the 'return' with a 'print', you could observe that Python
#                 # will try to helpfully unpack each value in the x, y and z tuple and format those.
#                 # Problem is, it will unpack each element in the item list, so in the first run,
#                 # the result in the for loop will be something like x = 10, y = 20 and z = 40.
#                 # That might seem hard to explain, so I'll show you in the next code snippet.

#                 return "x: {}, y:{}, z:{}".format(x, y, z)


def assignment (*args):
	for i in args: 
		for x in item:
			if len(item) == 1:
			    for x in item:
			        return "x: {}".format(x)
			    elif len(item) == 2:
			        for x, y in item:
			            return "x: {}, y:{}".format(x, y)
			    elif len(item) == 3:
			        for x, y, z in item:
			            return "x: {}, y:{}, z:{}".format(x, y, z)

#assignment again
f = [(10, 20, 30), (10, 40) , (4, 5, 20)] 
print vary_loops(f)
# '''
# x: 10, y: 20, z: 40
# x: 10, y: 40
# ...
# '''
# #l = [x, y, z]

# # for item in f:
# # 	#length = len(item)
# # 	#b = str(item)
# # 	for n in item: 
# # 		print assignment('x',n)
# # 	print (''),
# def vary_loops(*args):
#     for item in args:
#         if len(item) == 1:
#             for x in item:
#                 return "x: {}".format(x)
#         elif len(item) == 2:
#             for x, y in item:
#                 return "x: {}, y:{}".format(x, y)
#         elif len(item) == 3:
#             for x, y, z in item:
#                 return "x: {}, y:{}, z:{}".format(x, y, z)

# print vary_loops([(10,20,40), (23,45), (23,45,67)])