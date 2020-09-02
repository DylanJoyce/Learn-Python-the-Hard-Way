from sys import argv

script, filename = argv

txt = open(filename)
x = txt.read()

print x