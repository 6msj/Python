import pdb


def merge(A, p, q, r):
    """@todo: Docstring for merge

    :A: @todo
    :p: @todo
    :q: @todo
    :r: @todo
    :returns: @todo

    """
    n1 = q - p
    n2 = r - q
    L = []
    R = []
    for i in range(0, n1):
        L.append(A[p + i - 1])
    for j in range(0, n2):
        R.append(A[q + j])
    print L
    print R
    pdb.set_trace()  # XXX BREAKPOINT
    pass


def merge_sort(A, p, r):
    """@todo: Docstring for merge_sort

    :A: @todo
    :p: @todo
    :r: @todo
    :returns: @todo

    """
    if p < r:
        q = (p + r) / 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


def main():
    a_list = [1, 2, 12, 11, 13, 144, 22, 1, 8, 10]
    merge_sort(a_list, 0, len(a_list))
    #print a_list

main()
