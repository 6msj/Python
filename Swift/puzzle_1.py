from random import randint

def quicksort(list):
    if(len(list) <= 1):
        return list
    pivot = [list.pop(randint(0, len(list)-1))] 
    pivot_date_city = pivot[0].split()
    less, more = [], []
    for value in list:
        date_city = value.split() # date_city is a list with this format ['number', 'city', '#']
        if date_city[0] <= pivot_date_city[0]: # only compare the dates
            less.append(value)
        else:
            more.append(value)
    return quicksort(less) + pivot + quicksort(more)

def event_stream(filename):
    with open(filename) as f:
        content = f.readlines()
    return quicksort(content)

for event in event_stream('file'):
    #update_model(event)
    print event



