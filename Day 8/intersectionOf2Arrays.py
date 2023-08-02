# this program to find the intersection between two arrays
def intersect(nums1,nums2):
    hashmap = {}
    result = []
    for num in nums1:
        hashmap[num] = hashmap.get(num,0)+1
    for num in nums2:
        if num in hashmap and hashmap[num]!=0:
            result.append(num)
            hashmap[nums1] -= 1
    return result
finalresult = intersect([1,2,3,4],[3,4,5,1])
print(finalresult)