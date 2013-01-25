def MergeSort(List):
    lengthList = len(List)
    if lengthList == 1:
        return List

    # Split the list into two
    ListA = [List[i] for i in range(0, lengthList/2)]
    ListB = [List[i] for i in range(lengthList/2, lengthList)]
    MergeSort(ListA)
    MergeSort(ListB)
    MergeList(List, ListA, ListB)

def MergeList(List, ListA, ListB):
    lengthA = len(ListA)
    lengthB = len(ListB)
    indexList = 0;
    indexA = 0;
    indexB = 0;

    while True:
        # if indexA == lengthA, put the rest of listb into list
        if indexA == lengthA:
            for i in range(indexB, lengthB):
                List[indexList] = ListB[i]
                indexList += 1
            break;

        # if indexB == lengthB, put the rest of ListA into List
        if indexB == lengthB:
            for i in range(indexA, lengthA):
                List[indexList] = ListA[i]
                indexList += 1
            break;

        # if A is less than B, put A into the List
        if ListA[indexA] < ListB[indexB]:
            List[indexList] = ListA[indexA]
            indexA += 1
        # else, put B into the List
        else:
            List[indexList] = ListB[indexB]
            indexB += 1
        indexList +=1


Listy = [1,2, 3, 4, 5, 6]
Unsorted = [1, 4, 2, 10, 7, 19]

MergeSort(Unsorted)
MergeSort(Listy)

print Unsorted
print Listy






    
