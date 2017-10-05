def merge_intervals(array):
    if len(array) == 0:
        return []
    # if not sorted, sort the array by the starting interval
    array = sorted(array)
    output = [array[0]]
    for start, end in array[1:]:
        last_start, last_end = output[-1]
        if start <= last_end:
            output[-1] = (last_start, max(end, last_end))
        else:
            output.append((start, end))
    return output

if __name__ == '__main__':
    array = input("Enter interval array: ")
    print(merge_intervals(array))