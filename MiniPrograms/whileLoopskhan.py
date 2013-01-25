#While Loops - Khan Academy




### Basic While Loop , compares an equivalent while loop and for loop
# This while loop calculates the sum of 0 through 9 (including 9) and places it in 
# the variable sum
sum=0
j=0
while j<10:
    sum = sum + j
    print sum,
    j = j+1

for i in range(10):
    sum = sum + i
    print sum,


### More Basic While Loops
print ""
variableToBeAppended = [1,2,3,4]
x = 5
while x>1:
    variableToBeAppended.append("x appended by 5")
    x = x - 1

print variableToBeAppended #the array/list variableToBeAppended will get four additional 
                            #strings added on
