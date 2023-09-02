def findcommon(arr1,arr2,n1,n2):
    i = 0
    j = 0
    while (i<n1 and j<n2):
        if(arr1[i]==arr2[j]):
            print(arr1[i])
            i += 1
            j += 1
        elif arr1[i]<arr2[j]:
            i += 1
        else:
            j += 1
            
arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]

n1 = len(arr1)
n2 = len(arr2)

output = findcommon(arr1,arr2,n1,n2)
print(output)
            