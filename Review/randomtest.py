import random

fruits = ['apple','banana','coconut']

print "random.choice"
for i in range(5):
	print random.choice(fruits)

print "random.sample"
for i in range(5):
	print random.sample(fruits, 1)
