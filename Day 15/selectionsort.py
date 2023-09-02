def selectionSort(arr,size):
    for ind in range(size):
        min_ind = ind
        for i in range(ind+1,size):
            if (arr[i]<arr[min_ind]):
                min_ind = i
        arr[ind],arr[min_ind] = arr[min_ind],arr[ind]
arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)