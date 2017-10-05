def move_zeros_to_left(array):
    if len(array) < 1:
        return
    readIndex = writeIndex = len(array) - 1
    while readIndex >= 0:
        if array[readIndex] != 0:
            array[writeIndex] = array[readIndex]
            writeIndex -= 1
        readIndex -=1
    
    while writeIndex >= 0:
        array[writeIndex] = 0
        writeIndex -= 1

def main():
    array = input("Enter array: ")
    move_zeros_to_left(array)
    print(array)

main()