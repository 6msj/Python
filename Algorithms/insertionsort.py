def insertion_sort(A):
    """@todo: Docstring for insertion_sort
    """
    for j in xrange(1, len(A)):
        key = A[j]
        # Insert A[j] into the sorted sequence A[1.. j-1].
        i = j - 1
        while i > 0 and A[i] > key:
            temp = A[i]
            A[i] = A[i + 1]
            A[i + 1] = temp
            i = i - 1
        A[i + 1] = key


def main():
    """@todo: Docstring for main
    """
    a_list = [1, 7, 10, 11, 2, 3, 11, 23, 45, 4, 111, 33, 5, 6]
    insertion_sort(a_list)
    print a_list


main()
