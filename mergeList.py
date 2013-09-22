def mergeList(aList, bList):
    """@todo: Docstring for mergeList.

    :aList: @todo
    :bList: @todo
    :returns: @todo

    """
    aIndex = 0
    bIndex = 0
    aLen = len(aList)
    bLen = len(bList)
    mergedList = []
    while aIndex != aLen and bIndex != bLen:
        if aList[aIndex] < bList[bIndex]:
            tryToAppend(mergedList, aList[aIndex])
            aIndex = aIndex + 1
        elif aList[aIndex] > bList[bIndex]:
            tryToAppend(mergedList, bList[bIndex])
            bIndex = bIndex + 1
        else:
            tryToAppend(mergedList, aList[aIndex])
            aIndex = aIndex + 1
            bIndex = bIndex + 1

    if not aList:
        addRestToMergedList(mergedList, bList, bIndex)
    if not bList:
        addRestToMergedList(mergedList, aList, aIndex)

    return mergedList


def addRestToMergedList(mergedList, restList, index):
    sizeList = len(restList)
    while index != sizeList:
        mergedList.append(restList[index])
        index = index + 1


def tryToAppend(mergedList, item):
    if not mergedList or mergedList[-1] != item:
        mergedList.append(item)


def main():
    aList = [10, 20, 21, 21, 33, 44, 55, 600, 7000, 8000]
    bList = [20, 30, 30, 400, 559, 652, 701, 80000]
    mergedList = mergeList(aList, bList)
    print mergedList


main()
