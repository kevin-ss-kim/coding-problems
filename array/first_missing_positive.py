# Finds the first missing positive number in an nums
def first_missing_positive(nums):
    # For each position in nums, compare the nums[i] and nums[i + 1]
    # If nums[i] > nums[i + 1], loop through the nums descendingly
    # such that nums[i] <= nums[i + 1]
    if len(nums) == 0: return 1
    for i in xrange(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            index = i
            while index >= 0:
                if nums[index] > nums[index + 1]:
                    temp = nums[index]
                    nums[index] = nums[index + 1]
                    nums[index + 1] = temp
                index -= 1
    print(nums)
    # Find where 1 starts. If not found, return 1
    # If found, make sure that the next element is 2, the one after that is 3, etc.
    # If not, return the number checked. If end of nums, return last element + 1
    num = 1
    for i in xrange(len(nums)):
        if nums[i] > 0:
            if nums[i] != num:
                return num
            else:
                num += 1
    return nums[len(nums) - 1] + 1


if __name__ == '__main__':
    nums = input("Enter nums: ")
    print(first_missing_positive(nums))