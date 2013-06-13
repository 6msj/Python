list = [1, 2, 3, 22, 11, 2222, 33, 44]


def mergesort(list):
    length = len(list)
    if length == 1:
        return list
    left = [list[i] for i in range(0, length / 2)]
    right = [list[i] for i in range(length / 2, length)]

    mergesort(left)
    mergesort(right)
    mergelist(list, left, right)
    return list


def mergelist(list, left, right):
    lenL, lenR = len(left), len(right)
    index, indexL, indexR = 0, 0, 0

    while True:
        if indexL == lenL:
            for i in range(indexR, lenR):
                list[index] = right[i]
                index += 1
            break

        if indexR == lenR:
            for i in range(indexL, lenL):
                list[index] = left[i]
                index += 1
            break

        if right[indexR] < left[indexL]:
            list[index] = right[indexR]
            indexR += 1
        else:
            list[index] = left[indexL]
            indexL += 1
        index += 1

print mergesort(list)
