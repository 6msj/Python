### Strings - Khan Academy
## len(variable)
## concatenation
## splitting, finding , replacing, evaluating functions

## Khan Examples
a = "My first test string" 
b = 'Another test string that I have defined'
c = "This is Sal's string"
#d = ' This is Sal's string'         ## doesn't work because it stops midway
d = 'My favorite word is "asparagus", what is yours?' ## works because it ends with a ' ' 
math_string = "3+4*2" 
expression_string = "a+' '+b' tiger'"

print a, b, c, d 

len(a) ##takes the length of a in characters

print len(a)  ##prints the length of a, which is 20 characters
                ##length = len

### len() examples
print "This will print the length of a", len(a)
print "This will print the length of b", len(b)
print "This will print the length of c", len(c)
print "This will print the length of d", len(d)
print "This will print the length of math_string", len(math_string)
print "This will print the length of expression_string", len(expression_string)

### for loop + len + array/lists
h = [a, b, c, d, math_string, expression_string] ### makes an array of previous variables

i = 0
while h[i] != h[5]:
    print len(h[i]) ## prints out the length of whatever is at index one
    i = i + 1       ## counter for i
print len(h[5])    ## the while loop stops before hitting the last index


### concatenation

a_with_b = a+b   ## merges the two strings together
print ("This will print two variables concatenated together"), a_with_b

print ""    ## empty space

b_with_a = b+a  ## merges two strings in the reverse
print "This will print two a and b reversed", b_with_a


### splitting, finding
b.split(' ')  ## splits b during every space
print b.split(' ')
print b.split('t')  ## splits the word every t, t dissapears


# finding
math_string.find('2') ## finds the variable and states where it's located ##unneeded
print math_string.find('2')

# replace
c.replace('i', 'o') ## replaces a variable with another one ##unneeded
print c.replace('i','o') ## c does not change

g = c.replace('i','o')
print 'This prints out g, which is equivalent to c.replace', g

# evaluating
print "This evalutes math_string", eval(math_string) #evalutes math_string
print "This evalutes math_string+'1', by concatenating the 1 towards the end.", eval(math_string+'1') ## the 1 gets added to the end
print "This will evaluate variables.", eval(expression_string) ## takes variables and then evalutates them
