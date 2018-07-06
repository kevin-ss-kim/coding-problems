def median(array1, array2):

    m, n = len(array1), len(array2)
    if m > n:
        array1, array2, m, n = array2, array1, n, m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) / 2
    while imin < imax:
        i = (imin + imax) / 2
        j = half_len - i
        if i < m and array2[j - 1] > array1[i]:
            # i is too small, increase i
            imin = i + 1
        elif i > 0 and array1[i - 1] > array2[j]:
            # i is too big, decrease i
            imax = i - 1
        else:
            # found. Check for edge cases
            if i == 0: max_of_left = array2[j - 1]
            elif j == 0: max_of_left = array1[i - 1]
            else: max_of_left = max(array1[i - 1], array2[j - 1])
            if i == m: min_of_right = array2[j]
            elif j == n: min_of_right = array1[i]
            else: min_of_right = min(array1[i], array2[j])
            return (max_of_left + min_of_right) / 2.0

if __name__ == '__main__':
    array1 = input("Enter Array #1: ")
    array2 = input("Enter Array #2: ")
    print(median(array1, array2))