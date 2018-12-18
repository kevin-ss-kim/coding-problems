'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

def trap_rain_water(array):
    left, right, sum = 0, len(array) - 1, 0
    maxLeft, maxRight = 0, 0
    while left <= right:
        if array[left] <= array[right]:
            if array[left] >= maxLeft:
                maxLeft = array[left]
            else:
                sum += maxLeft - array[left]
            left += 1
        else:
            if array[right] >= maxRight:
                maxRight = array[right]
            else:
                sum += maxRight - array[right]
            right -= 1
    return sum