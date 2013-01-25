from sys import argv

script, input_file = argv

#functions

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

#main

current_file = open(input_file)

print "First ,let's print the whole file:\n"

print_all(current_file)

rewind(current_file)

print "Let's print three lines:"

current_line = 1

print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

