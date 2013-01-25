#Recursive Fibonacci Function - Khan Academy

def fibonacci(n):
    print ("fibonacci: "+ str(n)) #casts n as a string to add onto the print statement
    if n == 0 or n == 1:
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))

a = input
b = fibonacci(a)
print b
