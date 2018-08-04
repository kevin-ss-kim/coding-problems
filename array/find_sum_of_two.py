def find_sum_of_two1(array, target):
    # O(n) runtime, O(n) memory
    found_values = set()
    for e in array:
        if target - e in found_values:
            return True
        found_values.add(e)
    return False

def find_sum_of_two2(array, target):
    # O(n log n) runtime(sorting), O(1) memory
    array = sorted(array)
    low = 0
    high = len(array) - 1
    while low < high:
        sum = array[low] + array[high]
        if sum == target:
            return True
        if sum < target:
            low += 1
        else:
            high -= 1
    return False

if __name__ == '__main__':
    array = input("Enter array: ")
    value = input("Enter target value: ")
    print(find_sum_of_two1(array, value))