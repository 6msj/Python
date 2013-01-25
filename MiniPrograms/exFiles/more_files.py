from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line too, how?
input = open(from_file)
indata = input.read()

print "The input file is %d bytes long" % len(indata)   #len = length

print "Does the output file exists? %r" % exists(to_file)   #exists returns true if a file exists, based on the filename given
print "ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

output = open(to_file, 'w')     #opens the file with the 'w' being to write to it
output.write(indata)            #writes indata which was read from the first input file

print "Alright, all done."

output.close()      #closes output
input.close()       #closes input


#exercise 18
