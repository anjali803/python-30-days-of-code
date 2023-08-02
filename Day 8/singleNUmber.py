def singlenumber(nums):
    nums.sort()
    nums.append(0)
    i=0
    while i < len(nums):
        if nums[i]!=nums[i+1]:
            return nums[i]
        else:
            i = i+2
result = singlenumber([2,3,3])
print(result)