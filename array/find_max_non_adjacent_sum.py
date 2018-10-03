'''
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
'''

def find_max_non_adjacent_sum(array):
    inclusive = 0
    exclusive = 0
    for n in array:
        temp = inclusive
        inclusive = max(inclusive, exclusive + n)
        exclusive = temp
    return max(inclusive, exclusive)


if __name__ == '__main__':
    array = input("Enter array: ")
    print(find_max_non_adjacent_sum(array))