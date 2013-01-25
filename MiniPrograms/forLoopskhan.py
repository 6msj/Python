#For Loops - Khan Academy
#Range, a built in python function

###### range, print ranges range  formatforrange (start | stop | step)

print "This prints out a range of 6, which starts from 0 and ends at 5..range(6)", range(6)
print "This prints out a range of 7, which starts from 0 and ends at 6..range(7)", range(7)
print "This prints out a range from 1 - 7, but not including 7..range(7)", range(1,7)
print "This prints out a range from 2 - 8, but not including 8,,range(8)", range(2,8)
print "This prints out a range from 2 to 20, not including 20, incrementing by 3", range(2,20,3)
print "This prints out a range from 100-0, subtracting 20 incrementally", range(100,-1,-20)

###### for loop - basic loop
for i in range(5):              #remember the colon
    print i #prints out 0-4
for i in range(10):                 #remember the colon
    print i,                #prints out 0-9 #the , puts the numbers on the same line

print "\n"                      #new line
print "basic for loop has ended"

#### for loop - adding 
print "for loop - adding"
sum = 0
for i in range(10):                 #remember the colon
    sum = sum + i
    print sum,

#### for loop - subtracting
print ""
print "for loop - subtracting"
total = 100
for i in range(5):
    total = total - 20
    print total,
