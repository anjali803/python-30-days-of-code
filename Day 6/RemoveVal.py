# This program is to illustrate the removal of given val from an array nums
def RemoveVal(nums,val):
    index = 0
    for i in range(len(nums)):
        if (nums[i] != val):
            nums[index] = nums[i]
            index += 1
    return index
result = RemoveVal(nums=[1,2,2,3],val=3)
print(result)


