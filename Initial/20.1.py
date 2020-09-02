# import argv
from sys import argv

# sets values and syntax for call 
script, input_file = argv

# defines print_all, sets f as variable
def print_all(f):
#prints the read(out) of f
	print f.read()

# defines rewind, sets f as variable
def rewind(f):
#sets location to line 0 (i.e. the beginning the file)
	f.seek(0)
	
# defines print_a_line, sets line_count and f as variables
def print_a_line(line_count, f):
#prints line_count (what # line the program is at) and reads the line value
	print line_count, f.readline()

#sets current_file equal to open input file, i.e. current_file is an open input file that we can work w/
current_file = open(input_file)

print "First let's print the whole file:\n"

#runs print_all on current_file, the file we originally called opened
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#runs rewind on current_file
rewind(current_file)

print "Let's print three lines:"

#sets current_line equal to 1
n = 1
#runs print a line with current_line at 1
print_a_line(n, current_file)

#advances current_line to two
n += 1
#runs print a line with current_line a 2
print_a_line(n, current_file)

#advances current_line to three
n += 1
#runs print_a_line with current_line at 3
print_a_line(n, current_file)
