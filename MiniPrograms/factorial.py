#Writing A Simple Factorial Program - Khan Academy
# - factorial - 
# 1! = 1 , 2! = 2 * 1, 3! = 3 * 2 * 1, 4! = 4 * 3 * 2 * 1 -- and so on

#another basic for loop

number = input("Enter a non-negative interger to take the factorial of: ")              #string
product = 1 
for i in range(number):                  #range provides a list of numbers
    product = product * (i+1)
    
print product

###Defining a Factorial Function

#returns the factorial of the wrgument "number"
def factorial(number):
    product = 1 
    for i in range(number):                 
        product = product * (i+1)    
    return product


user_input = input("Enter a non-negative interger to take the factorial of: ")
factorial_of_user_input = factorial(user_input)
print factorial_of_user_input
