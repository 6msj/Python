def mergesort(A):
    """@todo: Docstring for mergesort

    :A: @todo
    :returns: @todo

    """
    length = len(A)
    if length == 1:
        return A
    left = [A[i] for i in range(0, length / 2)]
    right = [A[i] for i in range(length / 2, length)]
    mergesort(left)
    mergesort(right)
    merge(A, left, right)
    return A


def merge(A, left, right):
    """@todo: Docstring for merge

    :A: @todo
    :left: @todo
    :right: @todo
    :returns: @todo

    """
    lenL, lenR = len(left), len(right)
    indexA, indexL, indexR = 0, 0, 0
    while True:
        if indexL == lenL:
            for i in range(indexR, lenR):
                A[indexA] = right[i]
                indexA += 1
            break
        if indexR == lenR:
            for i in range(indexL, lenL):
                A[indexA] = left[i]
                indexA += 1
            break
        if right[indexR] < left[indexL]:
            A[indexA] = right[indexR]
            indexR += 1
        else:
            A[indexA] = left[indexL]
            indexL += 1
        indexA += 1


A = [122, 11, 133, 2323, 1, 2, 3, 44, 33, 22, 12, 23]

print mergesort(A)
