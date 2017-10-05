def binary_search(array, key):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) / 2
        if key > array[mid]:
            low = mid + 1
        elif key < array[mid]:
            high = mid - 1
        else:
            return mid
    return -1

def main():
    array = input("Enter sorted array: ")
    key = input("Enter key: ")
    print(binary_search(array, key))

main()