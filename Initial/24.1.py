print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love 
nor comprehend passion from intuition 
and requires an explanation
\n\t\twhere there is none.
"""

print "---------------"
print poem
print "---------------"

five = 10 - 2 + 3 - 6
print "This should be five : %s" % five

#defines function "secret_formula" that returns values for jelly_beans, jars and crates

def secret_formula(start):
	jelly_beans = start * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
	
start_point = 10000

#sets beans, jars and crates equal to the values returned by secret_formula when start_point is equal to 1000.

beans, jars, crates = secret_formula(start_point)

print "With a starting pint of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

#simplifies the above process by using the values already returned by secret_formula in the string, instead of variables that have to be defined on a separate line of code.
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)