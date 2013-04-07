from random import randint

list = [2,3,44,22,11,44,55,33]

def quicksort(list):
    if(len(list) <= 1):
        return list
    pivot = [list.pop(randint(0, len(list)-1))] 
    less, more = [], []
    for value in list:
        if(value <= pivot[0]):
            less.append(value)
        else:
            more.append(value)
    return quicksort(less) + pivot + quicksort(more)

print quicksort(list)
