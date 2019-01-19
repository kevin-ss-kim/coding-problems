'''
Given a robot cleaner in a room modeled as a grid.

Each cell in the grid can be empty or blocked.

The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made is 90 degrees.

When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell.

Design an algorithm to clean the entire room using only the 4 given APIs shown below.

interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}
'''

def cleanRoom(robot):
    visited = set()
    nextDirectionMap = {'u': 'r', 'r': 'd', 'd': 'l', 'l': 'u'}
    search(robot, (0,0), 'u', visited, nextDirectionMap)

def search(robot, pos, direction, visited, nextDirectionMap):
    robot.clean()
    visited.add(pos)
    for i in range(4):
        newPos = calculateNextPosition(pos, direction)
        if newPos not in visited and robot.move():
            search(robot, newPos, direction, visited, nextDirectionMap)
        robot.turnRight()
        direction = nextDirectionMap[direction]
    robot.turnRight()
    robot.turnRight()
    robot.move()
    robot.turnRight()
    robot.turnRight()

def calculateNextPosition(pos, direction):
    if direction == 'u':
        return pos[0] - 1, pos[1]
    elif direction == 'r':
        return pos[0], pos[1] + 1
    elif direction == 'd':
        return pos[0] + 1, pos[1]
    else:
        return pos[0], pos[1] - 1