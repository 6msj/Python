def binary_search(_list, key, imin, imax):
    """find the key within the _list"""
    if imax <= imin:
        return -1
    imid = (imin + imax) / 2

    if _list[imid] < key:
        # return the _list on the right of numbers greater than _list[imid]
        return binary_search(_list, key, imid + 1, imax)
    elif _list[imid] > key:
        # return the _list on the left of numbers less than _list[imid]
        return binary_search(_list, key, imin, imid - 1)
    else:
        return imid


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print binary_search(num_list,  12, 0, len(num_list))
