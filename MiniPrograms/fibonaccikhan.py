#Fibonacci Numbers - Khan Academy
# 0,1,1,2,3,5,8,13,21,34, .....
# Look up golden ratio
# 21/32 ~ close to golden ratio

def fibonacci(n):
    terms = [0,1]
    i = 2
    while i<=n:
        terms.append(terms[i-1]+terms[i-2])
        i = i + 1
    return terms[n]

print "Fibonacci Function"
print "Enter a number."
