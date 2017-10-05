def search_rotated_array(array, key):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) / 2
        if key > array[mid]:
            if array[mid + 1] <= key <= array[high]:
                low = mid + 1
            else:
                high = mid - 1
        elif key < array[mid]:
            if array[low] <= key <= array[mid - 1]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            return mid
    return -1

def main():
    array = input("Enter rotated array: ")
    key = input("Enter key: ")
    print(search_rotated_array(array, key))

main()