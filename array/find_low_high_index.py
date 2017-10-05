def find_low_high(array, key):
    low = 0
    high = len(array) - 1
    mid1 = mid2 = -1

    # Find low
    while low <= high:
        mid = (low + high) / 2
        if key > array[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if array[low] != key:
        return -1
    else:
        mid1 = low

    #Find high
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) / 2
        if key >= array[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if array[high] != key:
        return -1
    else:
        mid2 = high

    return (mid1, mid2)

def main():
    array = input("Enter sorted array: ")
    key = input("Enter key: ")
    print(find_low_high(array, key))

main()