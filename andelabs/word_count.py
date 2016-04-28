# a function that takes in a n input and gives a list of words
def word (b):
	'''
	This is a function that takes in a sentence.
	It gives an ouput of the words and frequency of appearence.
	'''
	a = b.split()

	wordfreq = []

	for w in a:
		wordfreq.append(a.count(w))

	print "String\n" + a +"\n"
	print "List\n" + str(a) + "\n"
	print "Frequencies\n" + str(wordfreq) + "\n"
	print "Pairs\n" + str(zip(a, wordfreq))

word("There is alot to do, to do")