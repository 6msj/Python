from random import randint


def quicksort(qlist):
    """ Quicksort """
    if(len(qlist) <= 1):
        return qlist
    pivot = [qlist.pop(randint(0, len(qlist) - 1))]
    less, more = [], []
    for value in qlist:
        if(value <= pivot[0]):
            less.append(value)
        else:
            more.append(value)
    return quicksort(less) + pivot + quicksort(more)

nlist = [2, 3, 44, 22, 11, 44, 55, 33]
print quicksort(nlist)
