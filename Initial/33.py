from sys import argv

script, n, z = argv

def number_lister(n):
	i = 0
	numbers = []
	
	for i in range(n):
		print "At the top i is %d" % i
		numbers.append(i)
	
		i += int(z)
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

number_lister(n)

print "The numbers: "

for num in numbers:
	print num