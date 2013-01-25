#reading from files, remember raw_input and argv

from sys import argv            #regular import, used to import argv

script, filename = argv         #argument to pass is filename

txt = open(filename)            #opening a file, in short you have to pass a file to run this script

print "Here's your file %r:" % filename     #reads from filename variable
print txt.read()                #reads the file
txt.close()

print "Type the filename again:"
file_again = raw_input("> ")        #new variable assigned to raw_input

txt_again = open(file_again)

txt.close()
print txt_again.read()
