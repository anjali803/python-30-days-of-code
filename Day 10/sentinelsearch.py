# Set the last element of the array to the target value. This is known as the sentinel value.
# Set the index variable “i” to the first element of the array.
# Use a loop to iterate through the array, comparing each element with the target value.
# If the current element is equal to the target value, return the index of the current element.
# Increment the index variable “i” by 1 after each iteration of the loop.
# If the loop completes and the target value is not found, return -1 to indicate that the value is not present in the array.
def sentinelSearch(arr,n,key):
    last = arr[n-1]
    arr[n-1] = key
    i = 0
    while(arr[i]!=key):
        i+=1
    arr[n-1]=last
    if(i<n-1)or(arr[n-1] == key):
        print(key,"elemet is found")
    else:
        print("element not found")
arr = [10,20,30,40,50,60,70,80]
n = len(arr)
key = 70
result = sentinelSearch(arr,n,key)
