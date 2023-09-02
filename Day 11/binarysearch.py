# implementation of binary search 
# arr = [2,5,8,12,16,23,38,56,72,91]


def binarySearch(arr,key):
    low = 0
    high = len(arr)-1
    mid = 0
    while(low<high):
        mid = (low+high)//2
        
        if arr[mid] < key:
            low = mid+1
        elif arr[mid] > key:
            high = mid-1
        else :
            return mid
    return -1
arr = [2,5,8,12,16,23,38,56,72,91]
key = 23
result = binarySearch(arr,key)
if (result!=-1):
    print("element found at the position",str(result))
    
else:
   print("element not found")