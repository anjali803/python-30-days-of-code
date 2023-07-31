#This program of array is to remove duplicates from sorted array
def RemoveDuplicates(nums):
    j = 1
    for i in range(1,len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    return j
nums=[1,2,1]
 
print(RemoveDuplicates(nums))

