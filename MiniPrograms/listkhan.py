#Python Lists - Khan Academy
#Lists or Arrays
#Basic If Statement

a = [1, -7, 0, 0, 5, 10]

#a[0] would be 1

if(a[0] > a[1]):
    print "since a[0] is greater than a[1], we will reset a[5] with 1"
    a[5] = 1
else: 
    print "nothing"

print a[5]

if(a[5] < a[4]):
    print "since a[5] is less than a[4], we will change a[3] to a word"
    a[3] = "word"
else:
    print nothing

print a[3]


######

###### deals with certain variables point to the same thing : sets c to point to the same thing as b

b = [1, 1, 1, 1, 1,] #declaring a list or array with only 1s in it
c = b                 #setting c to equal b, both point to the same thing
c[0] = 2                #changing index 0 to 2, so b[0] equals 2 also

print "this prints out b", b
print "this prints out c, which is the same as b", c

###### to copy elements from b, use this syntax a=b[:], to copy only up to a certain point
###### use this syntax, a=b[#:#], where # is any index of the array/list b

d=b[:]
print "d=b[:], this prints out d", d

e=b[0:2]
print "e=b[0:2], this prints out e, which takes the first and second index of b", e
e=b[0:3]
print "e=b[0:3], this prints out e again, which takes the first to third index of b", e

##### khan academy example
##### same stuff as above, + appending new elements
blah = [1, 2, -7, 9, 11]
print blah

blah[1] = "Sal's String"
print blah

sameasBlah = blah 
print "sameasBlah", blah

copyOfBlah = blah[:]
print "copyOfBlah", copyOfBlah

blah.append("new element") ##### appending

print blah #should have the new element "new elmement" at the end
print "this prints out b, which now gets the same element as blah", sameasBlah

print "this prints out copyOfBlah, it doesn't get the new element", copyOfBlah


asdf = [4, 4, 4,]
print asdf
