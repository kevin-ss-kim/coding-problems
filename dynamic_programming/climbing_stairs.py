'''
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
'''

def climbStairs(n, x):
    """
    :type n: int
    :rtype: int
    """
    return climbStairsWithMemo(n, {}, x)

def climbStairsWithMemo(n, array, x):
    if n < 0:
        return 0
    if n == 0:
        return 1
    elif n in array:
        return array[n]
    else:
        sum = 0
        for step in x:
            sum += climbStairsWithMemo(n - step, array, x)
        array[n] = sum
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
    n = input("Enter steps: ")
    x = input("Enter possible climb steps: ")
    print(climbStairs(n, x))