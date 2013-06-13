_list = [1, 2, 3, 123123, 22, 33, 4, 22, 11, 22323, 44]

# Compare from right to left.
# The bigger the index gets, the more compares you will have to do.


def insertion_sort(list):
    for index in range(1, len(list)):
        value = list[index]
        i = index - 1
        while i >= 0:
            if value < list[i]:
                list[i + 1] = list[i]
                list[i] = value
                i = i - 1
            else:
                break

insertion_sort(_list)

print _list
