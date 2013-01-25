# Printing
print "Hello World!"
print "Hello %r !" %r "World"

formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)

prompt = '> '
variable = raw_input(prompt)

# User Input
variable = raw_input()

# Importing
from sys import argv
script, input = argv

from os.path import exists
script, from_file, to_file = argv

# Functions
def functionname():
    print "Do something here"
def returnfunction(a,b):
    print "Something here"
    return a+b
def argsfunction(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# For Loop
for i in range(i):
    print "Do something here"
for i in range(1,5):
    print "Do something here."
    
# Files
input = open(filevariablename)
indata = input.read()
input.close()
output = open(filevariablename, 'w')
output.write(indata)
output.close()


# len = length

