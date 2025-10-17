
# recurive linear search
def linearSearchRecursive(l, x, i=0):
    if i == len(l):
        return False
    elif l[i] or linearSearchRecursive(l, x, i+1):
        return True

print("Recursive linear search result: ", linearSearchRecursive([1,2,3,4,5], 3))

#binary search
def binarySearch(L, x):
    low, high = 0, len(L)-1
    while low <= high:
        mid = (low + high)//2
        if L[mid] == x:
            return True
        elif L[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

print("Binary search result: ", binarySearch([1,2,3,4,5], 1))

#recursive binary search
def recursiveBinarySearch(L, x, low, high):
    mid = (high+low)//2
    if low > high:
        return False
    elif L[mid] == x:
        return True
    elif L[mid] < x:
        return recursiveBinarySearch(L, x, mid+1, high)
    else: # L[mid] > x:
        return recursiveBinarySearch(L, x, low, mid-1)
    
a = [1,2,3,4,5]
print('Recursive binary search: ', recursiveBinarySearch(a, 4, 0, len(a)-1))