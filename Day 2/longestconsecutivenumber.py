# Python program to find the longest consecutive number from a list
def longestconsecutivenum(nums):
    numset = set(nums)
    longest = 0
    for n in nums:
        if (n-1) not in numset:
            length = 0
            while (n+length) in numset:
                length += 1
                longest = max(length,longest)
    return longest
nums=[100,4,200,1,2,3,5,6]
print(longestconsecutivenum(nums))