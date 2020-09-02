#!/usr/bin/env python3

i = 0
numbers = []

print('\n')

while i < 6:
	print('At the top i is %d' % i)
	numbers.append(i)

	i += 1
	print('Numbers now: '), numbers
	print('At the bottom i is %d. \n' % i)

print('The numbers: ')

for num in numbers:
	print(num)