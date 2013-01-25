x = "There are %d types of people." % 10 #assigns a string to x
binary = "binary" #assigns the word binary to the variable binary
do_not = "don't" #assigns the word don't to the variable do_not
y = "Those who know %s and those who %s." % (binary, do_not) #replaces %s and %s with the two variables
print x #prints out the variable x which contains a string
print y #prints out the variable y which contains a string 

print "I said %r." % x #prints out %r which is replaced by x which contains a string
print "I also said: '%s'." % y #prints out %s which is y which is a string within ' '

hilarious = False # assigns a value of False to the variable hilarious
joke_evaluation = "Isn't that joke so funny?! %r" #makes joke_evaluation a string that includes a variable %r

print joke_evaluation % hilarious #prints the joke evaluation and replaces the %r with the variable hilarious

w = "This is the left side of ... " #variable string
e = "a string with a right side." #variable string

print w + e #prints out both w and e in succession
