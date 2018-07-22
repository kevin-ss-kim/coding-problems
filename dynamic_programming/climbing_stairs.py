def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    array = [None] * (n + 1)
    return climbStairsWithMemo(n, array)
def climbStairsWithMemo(n, array):
    if n < 0:
        return 0
    if n == 0:
        return 1
    elif array[n] != None:
        return array[n]
    else:
        array[n] = climbStairsWithMemo(n - 1, array) + climbStairsWithMemo(n - 2, array)
        return array[n]

if __name__ == '__main__':
    n = input("Enter number of steps: ")
    print(climbStairs(n))