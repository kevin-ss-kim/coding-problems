def find_smallest_common_number(arrays):
    a = arrays[0]
    b = arrays[1]
    c = arrays[2]
    i = j = k = 0
    while i < len(a) and j < len(b) and k < len(c):
        if a[i] == b[j] and b[j] == c[k]:
            return a[i]
        if a[i] <= b[j] and a[i] <= c[k]:
            i += 1
        elif b[j] <= a[i] and b[j] <= c[k]:
            j += 1
        elif c[k] <= a[i] and c[k] <= b[j]:
            k += 1
    return -1

def main():
    count = 1
    arrays = []
    while count <= 3:
        array = input("Enter sorted array #%s: " % count)
        arrays.append(array)
        count += 1
    print(find_smallest_common_number(arrays))

main()