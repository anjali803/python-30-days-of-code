# In binary search the items in the list will be sorted in increasing or decreasing order 
def binarysearch(list,value):
    low = 0
    high = len(list)-1
    mid = 0
    
    while(low<high):
        mid = (low + high)//2
        if list[mid] < value:
            low = mid + 1
        elif list[mid] > value:
            high = mid - 1
        else:
            return mid
    return -1
list = [10,20,30,40,50]
value = 30 
result = binarysearch(list,value)
if result != -1:
    print("item present at :",str(result))
else:
    print("Element not found!")
      