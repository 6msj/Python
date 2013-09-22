def call_sort(sort, unsortedList):
    return eval(sort)(unsortedList)


def insertion_sort(s):
    n = len(s)
    for i in range(0, n):
        j = i
        while (j > 0 and s[j] < s[j - 1]):
            s[j], s[j - 1] = s[j - 1], s[j]
            j = j - 1
    return s


def selection_sort(s):
    n = len(s)
    for i in range(0, n):
        min = i
        for j in range(i + 1, n):
            if s[j] < s[min]:
                min = j
        s[i], s[min] = s[min], s[i]
    return s


sort = "insertion_sort"
sort = "selection_sort"
unsortedList = [1, 2, 13, 41, 12, 18, 19, 22]
print call_sort(sort, unsortedList)
