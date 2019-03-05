'''
https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. 
Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. 
You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).
'''

def knapsack(val, wt, W):
    return helper(val, wt, W, len(val) - 1, {})

def helper(val, wt, wt_left, i, cache):
    # Base case
    if wt_left <= 0 or i == 0:
        return 0
    # Use cache to speed things up
    if i in cache:
        return cache[i]
    # Find the maximum of including the current item or excluding the current item
    cache[i] = max(
        helper(val, wt, wt_left, i - 1, cache),
        wt[i] + helper(val, wt, wt_left - wt[i], i - 1, cache)
    )
    return cache[i]