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
    # Initialize number to check against to 1
    # Loop through the array and find find the positive number
    # If greater than the number checked against, return the checked number
    # If not, increment the checked number if it is equal
    # If end of nums, return last element + 1
    num = 1
    for i in xrange(len(nums)):
        if nums[i] > 0:
            if nums[i] > num:
                return num
            elif nums[i] == num:
                num += 1
    return nums[len(nums) - 1] + 1


if __name__ == '__main__':
    nums = input("Enter nums: ")
    print(first_missing_positive(nums))