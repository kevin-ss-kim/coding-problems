import random

def partition(array, low, high):
    pivot_index = random.randint(low, high)
    pivot_value = array[pivot_index]
    array[high], array[pivot_index] = array[pivot_index], array[high]
    i = low - 1
    # Move pivot to the correct spot
    for j in range(low, high):
        if array[j] <= pivot_value:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quicksort(array, low, high):
    if low < high:
        # Choose pivot index
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)

if __name__ == '__main__':
    array = input("Enter array: ")
    quicksort(array, 0, len(array) - 1)
    print(array)