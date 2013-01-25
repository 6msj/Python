def Compare(left, right):
    if left < right:
        return -1
    if left == right:
        return 0
    return 1

def QSort(List):
    QuickSort(List, 0, len(List)-1)

def QuickSort(List, left, right):
    # base case
    if right <= left or len(List) == 1:
        return

    # set pivot
    pivot = List[left]
    l = left
    r = right







