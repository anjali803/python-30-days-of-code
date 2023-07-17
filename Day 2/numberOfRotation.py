# given a rotated sorted list that was rotated for unknow number of times , we need to find the number of times it was rotated
# On implementing linear search we can solve this - thus the time complexity will be O(N)
# but we need to get a complexity of O(logn)-so this program will be agian modified

def rotationCountLinearsearch(nums):
    position = 0
    while (position < len(nums)):
        if position > 0 and nums[position] < nums[position-1]:
            return position
        position += 1
    return 0
nums=[5,6,1,2,3,4]
print(rotationCountLinearsearch(nums))