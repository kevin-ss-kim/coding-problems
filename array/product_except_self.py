def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    left, right, rtnArray = [None] * len(nums), [None] * len(nums), [None] * len(nums)
    leftIndex, rightIndex, productLeftSoFar, productRightSoFar = 0, len(nums) - 1, 1, 1
    while leftIndex < len(nums):
        productLeftSoFar *= nums[leftIndex]
        productRightSoFar *= nums[rightIndex]
        left[leftIndex], right[rightIndex] = productLeftSoFar, productRightSoFar
        leftIndex += 1
        rightIndex -= 1
    for i in xrange(len(nums)):
        if i == 0:
            rtnArray[i] = right[i + 1]
        elif i == len(nums) - 1:
            rtnArray[i] = left[i - 1]
        else:
            rtnArray[i] = left[i - 1] * right[i + 1]
    return rtnArray

if __name__ == '__main__':
    array = input("Enter array: ")
    print(productExceptSelf(array))