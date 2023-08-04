# [10,20,30,40,50,60,70,80] = elments of the array
# key = 60
# return the element

def linearSearch(arr,n,key):
    for i in range(n):
        if (arr[i] == key):  #elemt should be equal to the key than return the position of that element
            return i
    return -1
arr = [10,20,30,40,50,60,70,80]
n=len(arr)
key = 60
result = linearSearch(arr,n,key)  #output : 5
if (result == -1):
    print("Element is not present")
else:
    print("Elment present at the position",result)
        