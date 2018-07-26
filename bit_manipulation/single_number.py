def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ones = 0
    twos = 0

    for i in xrange(len(nums)):   
        x = nums[i]
        twos |= ones & x
        ones ^= x
        not_threes = ~(ones & twos)
        ones, twos = ones & not_threes, twos & not_threes
    return ones

if __name__ == '__main__':
    array = input("Enter array: ")
    print(singleNumber(array))