def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    return climbStairsWithFibonacci(n)

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

def climbStairsWithFibonacci(n):
    if n == 1:
        return 1
    first, second = 1, 2
    for i in xrange(3, n + 1):
        third = first + second
        first = second
        second = third
    return third

if __name__ == '__main__':
    n = input("Enter number of steps: ")
    print(climbStairs(n))