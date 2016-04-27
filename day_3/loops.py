a = [10, 40, -9 , 45, 60, 89]

for i in a:
	print i

#print in reverse

i = len(a)

while i > 0:
	print a[i-1]
	i -= 1

for index in range(len(a)-1, -1, -1): 
	print a[index]

b = [(2, 4), (5, 10), (6,20), (50, 50)]
'''
x: 2 , y: 2
'''
for i in b:
	print "x: {} , y: {}".format(*i)

for x, y in b:
	print "x:{} , y:{}".format(x, y)

for item in b:
	print "x:{} , y:{}".format(item[0], item[1])

a = [(3, 4, 5) ,(4, 5, 6)]

for a, b, c in a:
	print "a:{} , b:{} , c:{}".format(a, b, c)

