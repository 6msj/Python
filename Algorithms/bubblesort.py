def bubblesort(A):
    """@todo: Docstring for bubblesort

    :A: @todo
    :returns: @todo

    """
    for i in xrange(0, len(A) - 1):
        for j in xrange(len(A) - 1, i, -1):
            if A[j] < A[j - 1]:
                temp = A[j]
                A[j] = A[j - 1]
                A[j - 1] = temp
    return A


a = [1, 2, 33, 22, 11, 23, 4, 33, 55, 33, 221, 3]
print bubblesort(a)
