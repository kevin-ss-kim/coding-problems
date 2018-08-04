# Finds the first missing positive number in an array
def first_missing_positive(array):
    # For each position in array, compare the array[i] and array[i + 1]
    # If array[i] > array[i + 1], loop through the array descendingly
    # such that array[i] <= array[i + 1]
    
    # Find where 1 starts. If not found, return 1
    # If found, make sure that the next element is 2, the one after that is 3, etc.
    # If not, return the number checked. If end of array, return last element + 1
    return 1


if __name__ == '__main__':
    array = input("Enter array: ")
    print(first_missing_positive(array))