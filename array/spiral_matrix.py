'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

'''

def spiral_matrix(matrix):
    if not matrix: return []
    output = []
    row_begin, row_end = 0, len(matrix) - 1
    col_begin, col_end = 0, len(matrix[0]) - 1
    while row_begin <= row_end and col_begin <= col_end:
        # Right
        for i in range(col_begin, col_end + 1):
            output.append(matrix[row_begin][i])
        row_begin += 1
        for i in range(row_begin, row_end + 1):
            output.append(matrix[i][col_end])
        col_end -= 1
        if row_begin < row_end:
            for i in range(col_end, col_begin - 1, -1):
                output.append(matrix[row_end][i])
            row_end -= 1
        if col_begin < col_end:
            for i in range(row_end, row_begin - 1, -1):
                output.append(matrix[i][col_begin])
            col_begin += 1
    return output