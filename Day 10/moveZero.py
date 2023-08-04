# in a given array the number of zeros occuring should be moved to the end of the array
def MoveZero(nums):
    i = 0
    while (i<len(nums)):
        if(nums[i]==0):
            nums.append(0)
            nums.remove(0)
        i+=1
    return nums

result = MoveZero([1,0,3,0])
print(result)