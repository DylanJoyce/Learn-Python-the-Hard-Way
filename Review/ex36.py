#from sys import argv
import time
import random

#script, x = argv

def start():

	print "Life is chaotic. Rules exist, but may not be obvious to those within a chaotic system."
	
	time.sleep(1)
	
	print "And even suggesting that we live in chaos assumes that there is no true randomness in our world system! And there might be!"
	
	time.sleep(1)
	
	print "Anyway..."
	
	time.sleep(1)
	
	number_fun()

def number_fun():
	get_number()
	process_number()

def get_number():

	y = int(raw_input("Pick a number! "))
	x = int(raw_input("Good. Pick another! "))
	
	#generates random integer between 0 and 9, inclusive
	r = random.randint(0,10)
	#creates integers out of x and y so we can work with everything mathematically as integers
	
	#multiplies x by y, divides by r, sets number equal to remainder
	global number 
	number = (x*y+r)%10
	number = int(number)
	print "Your resulting number is %d." % number
	return number

def process_number():

	if number%2 == 0:
		print "Oh good, now we can play the next game!"
		print """ 
			Fist bump of encouragement!
						 
				  .``..``..``..``.
				  (( ) ( )(  )(  ))
				  |  |   |   |   | \
				  |  |   |   |   |  \
				  \__|___|___|___//_ )
							((__|;;  )
							 -------- 
		"""
		list_battle()
	
	else:
		print "Sometime's life is odd. It will make you wait for what seems like no reason at all."
		time.sleep(number)
		print "Try again!"
		
		number_fun()
		

def list_battle():

	print "Let's see what can make the stronger list: a computer or a human."
	
	number_list1 = []
	number_list2 = []
	
	for i in range(0,9):
		z = random.randint(0,5) 
		number_list1.append(z)
		
	for b in range(0,9):
		q = raw_input("Pick a number between 5 and 15. ")
		q = int(q)
		
		if q >= 5 and q <=15:
			number_list2.append(q)
		else:
			exit("That's not between 5 and 15! We will never beat the machines unless we pay attention!")
		
	print "The computer generated list is as follows: " + str(number_list1) + "."
	print "The list you generated is as follows: " + str(number_list2) + "."
	
	if sum(number_list1) > sum(number_list2):
		print "\nNumber list 1 wins! Go computers!"
	
	elif sum(number_list1) < sum(number_list2):
		print "\nNumber list 2 wins! Go sentients!"
		
	else:
		print "The Singularity is upon us!"
		
start()


