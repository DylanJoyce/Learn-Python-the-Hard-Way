# Dylan N. Joyce

import random 
import textwrap 
import time

#creates empty dictionary kitty_qualities to be filled in by user input
#in NameKitten
kitty_qualities = {}

class Game(object):

	def __init__(self, start): self.start = start

	def play(self): 
		next_room_name = self.start
		
		while True: 
			room = getattr(self, next_room_name) 
			next_room_name = room()

	def DarkRoom(self):
		#overwrought prose 
 		prose = "Breathing shortly and sharply as your eyes search\
 		frigid pure darkness for any vision, no sooner do you ask how\
 		long you've been awake then your hands reflexively grip your\
 		head's both sides to alleviate an impossible  pressure bearing\
 		down on your skull like an ocean on a tinfoil submarine. You\
 		pray for rupture that does not come."

		#print '\n'.join(textwrap.wrap(prose, 70))
		print '{:*^70}'.format(prose)
 		time.sleep(7)

 		prose = "Does the agony expand and contract in your desperately\
 		beating heart? Or does the darkness itself birth it thick and \
 		steady? Time measures activity; does this agony move? Later, \
 		somewhere else, you might remember yourself imagining this \
 		moment and name it Agony. This is to survive and deny. But \
 		no such thought can enter your head now as the splitting \
 		sensation expands in all directions. This agony is neither \
 		known nor told--it endures and is endured."

 		time.sleep(random.randint(0,10))

 		print "But after forever a light cleanly clicks dim, time
 		returns, and as your brain" print "regains itself, the question
 		comes: \"But what else?\"\n"

		return 'LightRoom'

	def LightRoom(object): first_move = raw_input("So? ")

 		if first_move == "look around": print "You see your frosty
 		breath and tiny hairballs. Interesting..." return
 		'LightRoomCorner' elif first_move == "listen": print "A soft
 		purring is heard. Interesting..." return 'LightRoomCorner'
 		else: print "Does not compute!" return 'LightRoom'

	def LightRoomCorner(object):

 		second_move = raw_input("So what do you want to do? ")

 		if second_move == "investigate": print "Huddled in the corner
 		is a large litter of wee newborn kittens." return 'NameKitten'
 		else: print "Does not compute." return 'LightRoomCorner'

	def NameKitten(object):

		#lists adjectives to describe the kittens that the user will name
		nice_adj = ['darling', 'precious', 'nice', 'beautiful',
		'lovely'] kitten_color = ['black', 'grey', 'brindle', 'gold',
		'white'] eye_color = ['blue', 'green', 'gold']

		print "Name the kittens!"

		kitty_count = 1

		while kitty_count < 4:

			#each of the below picks a random string from the adjective
			#lists above
			rand_nice_adj1 = nice_adj[random.randint(0,
			len(nice_adj)-1)] rand_nice_adj2 =
			nice_adj[random.randint(0, len(nice_adj)-1)] rand_nice_adj3
			= nice_adj[random.randint(0, len(nice_adj)-1)]
			rand_kitten_color = kitten_color[random.randint(0,
			len(kitten_color)-1)] rand_eye_color =
			eye_color[random.randint(0, len(eye_color)-1)]

			#creates naming prompt here so it can be inserted cleanly
			#into the name = raw_input()
			prompt = "Name kitten #%d! It is a %s litte %s kitten with
			%s %s eyes. " %( kitty_count, rand_nice_adj1,
			rand_kitten_color, rand_nice_adj2, rand_eye_color)

			name = raw_input(prompt)

			print "Oh, that's a %s name! Hello %s" % (rand_nice_adj3,
			name)

			#adds one to the count

			#adds name, kitten color, eye color to dictionary
			#kitty_qualities with kitty_count as key
			kitty_individual_attributes = {}
			kitty_individual_attributes['kitten_number'] = kitty_count
			kitty_individual_attributes['name'] = name
			kitty_individual_attributes['kitten_color'] =
			rand_kitten_color kitty_individual_attributes['eye_color'] =
			rand_eye_color kitty_qualities[kitty_count] =
			kitty_individual_attributes print kitty_qualities
			kitty_count += 1

# 			for i in (kitty_count, name, rand_kitten_color,
# 			rand_eye_color): kitty_qualities = locals(i)

		#rand_kitten = random.randint(########)
		print "As her siblings look on, one especially brave kitten\
		marches up and, after a brief but seriously executed\
		inspection, rubs lovingly against your leg. The others,\
		emboldened by her kindness, approach and do the same. Soon you\ 
		are surrounded!" 
		
		time.sleep(2) 
		
		print "Since the frigid cold has sucked all energy out of you and\
		the kittens melted any resistance you might have otherwise\
		marshalled against exhaustion, you lie down, and fall asleep as the\
		wee kittens place themselves atop you, sharing their warmth." 
		
		time.sleep(1) 
		
		print "But shortly later you wake up shivering. These kittens are\ 
		too small to keep you warm."
		
		time.sleep(1) print "...like this."

		return 'KittenActivity'

	def KittenActivity(object):

		prompt = "So what to do? "

		third_move = raw_input(prompt)

		if third_move == "snuggle": print "You try to snuggle, but the
		cold becomes impossible to ignore. If you" print "do not act
		soon, you will have no energy left." return 'KittenActivity'
		elif third_move == 'punch' or third_move == 'kick': print "In
		your frustration, you %s one of the kittens. You're just an
		asshole. You die." % third_move exit(1) elif third_move == "skin
		'em and make a coat": print "You're an asshole, but one that
		understands the current value of heat. You" print "carefully
		remove the outermost kitten and gently smother the wee creature,"
			#! add part where each kitten is named and described as the
			#borderline psychopathic user kills it
			print "repeating the process until only one remains. You
			attack this kitten, but" print "as its claws extend to
			defend itself, you simultaneously snap its neck" print "and
			tiny wrist, locking the feline corpse's claws in place."
			time.sleep(1) print "As tears silent trace ice trails down
			your face, you skin the kitten with their sibling's" print
			"own claw." time.sleep(1) print "You sick bastard. You
			survive, but at what price?"
			# In this environment there is only one way to skin a cat.
			time.sleep(2) print "Their fur is so soft." exit(1)

a_game=Game("DarkRoom") a_game.play()