# def rotate_array(array, amount):
#     newArray = []
#     for i in xrange(0,len(array)):
#         newArray.append(array[(i - amount) % len(array)])
#     return newArray

def reverse_array(array, start, end):
    while start < end:
        temp = array[start]
        array[start] = array[end]
        array[end] = temp
        start += 1
        end -= 1

def rotate_array(array, amount):
    amount = amount % len(array)
    reverse_array(array, 0, len(array) - 1)
    reverse_array(array, 0, amount - 1)
    reverse_array(array, amount, len(array) - 1)
    return array

def main():
    array = input("Enter array: ")
    key = input("Enter number of rotations: ")
    print(rotate_array(array, key))

main()