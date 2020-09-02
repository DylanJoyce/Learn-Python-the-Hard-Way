#!/usr/bin/env python

the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number
print('\n')

# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit
print('\n')
# also we can go through mixed list too
# notice we have to use %r since we don't what's in it
for i in change:
	print("I got %r" % i)
print('\n')
# we can also build lisets, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range[6]:
	print("Adding %d to the list." %i)
	# append is a function that lists
	elements.append(i)
print('\n')
# now we can pritn them out too
for i in elements:
	print("Element was: %d" % i)