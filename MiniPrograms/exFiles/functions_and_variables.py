def bubbleSort(numArray):
    for i in range(5):
        lowest = numArray[i]
        for j in range(5):
            if(lowest<numArray[j]):
                placeholder = numArray[i]
                numArray[i] = numArray[j]
                numArray[j] = placeholder
    print numArray


numOne = []
for i in range(5):
    num = raw_input("Enter a number.: ")
    numOne.append(num)
for i in range(5):
    print "The list is " + numOne[i] + "."
bubbleSort(numOne)


#########################################################################

def cheese_and_crackers(cheese_count, boxes_of_crackers):       #defines a function that prints statement depending on the variables given
    print "You have %d cheeses!" % cheese_count
    print "you have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the functions numbers directly:"
cheese_and_crackers(20,30)                          #uses the above function and gives two values directly as arguments

print "OR, we can use variables from our script:"
amount_of_cheese = 10                   #gives a value to the variables
amount_of_crackers = 50                 #same

cheese_and_crackers(amount_of_cheese, amount_of_crackers)     #another function

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
