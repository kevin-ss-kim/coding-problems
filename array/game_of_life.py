'''
Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.
'''

def game_of_life(board):
    '''
    type board: list[list[int]]
    '''
    hashSet = set()
    max_x = len(board) - 1
    max_y = len(board[0]) - 1
    for x in range(len(board)):
        for y in range(len(board[x])):
            neighbors = [
                getVal(x-1,y-1,max_x,max_y,board,hashSet),
                getVal(x-1,y,max_x,max_y,board,hashSet),
                getVal(x-1,y+1,max_x,max_y,board,hashSet),
                getVal(x,y-1,max_x,max_y,board,hashSet),
                getVal(x,y+1,max_x,max_y,board,hashSet),
                getVal(x+1,y-1,max_x,max_y,board,hashSet),
                getVal(x+1,y,max_x,max_y,board,hashSet),
                getVal(x+1,y+1,max_x,max_y,board,hashSet),
            ]
            neighbor_count = sum(1 if n == 1 else 0 for n in neighbors)
            if board[x][y]:
                if neighbor_count < 2 or neighbor_count > 3:
                    hashSet.add((x,y))
                    board[x][y] = 0
            else:
                if neighbor_count == 3:
                    hashSet.add((x,y))
                    board[x][y] = 0

def getVal(x, y, max_x, max_y, board, hashSet):
    if x < 0 or y < 0 or x > max_x or y > max_y:
        return -1
    if (x,y) in hashSet:
        if board[x][y]:
            return 0
        else:
            return 1
    return board[x][y]