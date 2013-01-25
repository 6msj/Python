def factorial(number):
    if number <= 1:         #base case
        return 1
    else:
        return number *factorial(number-1)

user_input = input("Enter a non-negative interger to take the factorial of: ")
factorial_of_user_input = factorial(user_input)
print factorial_of_user_input


#Iterative
def factorial(number):
    product = 1
    for i in range(number):
        product = product * (1+1)
    return product

#Recursive
def factorial(number):
    if number <=1 #base case
        return 1
    else:
        return number*factorial(number-1)
