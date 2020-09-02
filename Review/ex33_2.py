from sys import argv

script, n = argv

i = 0
numbers = []

def number_lister(n):
	for i in range(int(n)):
		print "At the top i is %d" % i
		numbers.append(i)
	
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

number_lister(n)

print "The numbers: "

for num in numbers:
	print num