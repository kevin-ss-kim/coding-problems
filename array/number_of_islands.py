'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

'''

def dfs_explore(grid, x, y):
    if (x < len(grid) and y < len(grid[x]) and grid[x][y] == 1):
        grid[x][y] = 0
        dfs_explore(grid, x + 1, y)
        dfs_explore(grid, x, y + 1)

def num_islands(grid):
    num_islands = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 1:
                num_islands += 1
                dfs_explore(grid, x, y)
    return num_islands