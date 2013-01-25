#Writing a Sorting Function - Khan Academy

#There's a function in python that will sort the list ".sort()"
#Bubble Sort

a = [7,1,3,5,2,8]

print a
#a.sort()        #sorts the function

def leastToGreatest(a):
    for i in range(len(a)):         #this sorting function compares each index against
        for j in range(len(a)):       #every other index for the length of the index
            if a[i] < a[j]:             #compares index i against index j
                placeholder = a[i]
                a[i] = a[j]
                a[j] = placeholder
                

    print a

leastToGreatest(a)


#Khan Academy's Sort
#Insertion Sort
#Algorithm - A process/method/way to do something

def insertion_sort(list):
    for index in range(1,len(list)):
        value = list[index]
        i = index - 1
        while i>=0:                 #as the loop moves to the right of the array, it has to check more times
            if value < list[i]:
                list[i+1] = list[i] #shift the number to the right, since value is checking to the left
                list[i] = value     #value is shifted to the left, because it is less than the number it was checking to the left
            else:
                break
