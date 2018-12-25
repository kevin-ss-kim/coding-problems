'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
'''

def find_kth_largest(nums, k):
    hashMap = collections.defaultdict(int)
    for num in nums:
        hashMap[num] += 1
    hashMap = collections.OrderedDict(sorted(hashMap.items(), reverse=True))
    element = 0
    for key in hashMap:
        count = hashMap[key]
        while k > 0:
            if count == 0:
                break
            element = key
            count -= 1
            k -= 1
        if k == 0:
            break
    return element