name = "Dylan Joyce"
age = 35 # a lie
height = 73 # inches
weight = 180 # lbs
eye_color = "blue"
teeth_color = "white"
hair_color = "dirty blondish"

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eye_color, hair_color)
print "His teeth are usually %s depending on the coffee." % teeth_color

# this line is trikcy, try to get it exactly right
print "If I add %d, %d, and %d, I get %d." % (
	age, height, weight, age + height + weight)
