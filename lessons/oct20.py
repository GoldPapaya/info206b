# selection sort O(n^2)
def selectionSort(lst):
    for i in range(len(lst)-1):
        minVal = lst[i]
        indexSmallest = i
        for j in range(i+1, len(lst)):
            if lst[j] < minVal:
                minVal = lst[j]
                indexSmallest = j
        temp = lst[i]
        lst[i] = minVal
        lst[indexSmallest] = temp
    return lst

print(selectionSort([5,4,3,2,1]))

# merge sort (need to implement merge subfxn) O(nlog(n))
def mergeSort(lst, p, r):
    if p == None and r == None:
        p = 0
        r = len(lst)-1

    def merge(lst, p, q, r):
        # some fxn that performs the merge for 2 lists.
        pass
    
    if p < r:
        q = (p+r)/2
        mergeSort(lst, p, q)
        mergeSort(lst, q+1, r)
        merge(lst, p, q, r)
