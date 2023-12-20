import sys

import numpy as np

def prettyPrint(touched, grid):
    for row,gr in zip(touched,grid):
        for t in row:
            if t:
                print('# ', end='')
            else:
                print('. ', end='')
        print('\t', end='')
        for g in gr:
            print(g + ' ', end='')
        print()

def stringify(laser):
    return '-'.join([str(laser[0][0]), str(laser[0][1]), str(laser[1]), str(laser[2])])


def hitsWall(grid, loc, dir):
    if dir == 'N':
        return loc[0] == 0
    if dir == 'S':
        return loc[0] == len(grid) - 1
    if dir == 'E':
        return loc[1] == len(grid[0]) - 1
    if dir == 'W':
        return loc[1] == 0

def laserize(grid, touched, loc, dir, changed):
    x = loc[0]
    y = loc[1]
    touched[x][y] = True
    # print(loc, dir)
    # prettyPrint(touched, grid)
    # print()
    if dir == 'N':
        if grid[x][y] == '/' and not changed:
            return touched, [[(x, y), 'E', True]]
        elif grid[x][y] == '\\' and not changed:
            return touched, [[(x, y), 'W', True]]
        elif grid[x][y] == '-' and not changed:
            return touched, [[(x, y), 'E', True], [(x, y), 'W', True]]
        elif hitsWall(grid, loc, dir):
            return touched, [[(-1, -1), 'B', True]]
        else:
            return touched, [[(x-1, y), 'N', False]]
    elif dir == 'S':
        if grid[x][y] == '/' and not changed:
            return touched, [[(x, y), 'W', True]]
        elif grid[x][y] == '\\' and not changed:
            return touched, [[(x, y), 'E', True]]
        elif grid[x][y] == '-' and not changed:
            return touched, [[(x, y), 'E', True],[(x, y), 'W', True]]
        elif hitsWall(grid, loc, dir):
            return touched, [[(-1, -1), 'B', True]]
        else:
            return touched, [[(x+1, y), 'S', False]]
    elif dir == 'E':
        if grid[x][y] == '/' and not changed:
            return touched, [[(x, y), 'N', True]]
        elif grid[x][y] == '\\' and not changed:
            return touched, [[(x, y), 'S', True]]
        elif grid[x][y] == '|' and not changed:
            return touched, [[(x, y), 'N', True],[(x, y), 'S', True]]
        elif hitsWall(grid, loc, dir):
            return touched, [[(-1, -1), 'B', True]]
        else:
            return touched, [[(x,y+1), 'E', False]]
    elif dir == 'W':
        if grid[x][y] == '/' and not changed:
            return touched, [[(x, y), 'S', True]]
        elif grid[x][y] == '\\' and not changed:
            return touched, [[(x, y), 'N', True]]
        elif grid[x][y] == '|' and not changed:
            return touched, [[(x, y), 'N', True],[(x, y), 'S', True]]
        elif hitsWall(grid, loc, dir):
            return touched, [[(-1, -1), 'B', True]]
        else:
            return touched, [[(x, y-1), 'W', False]]
    return touched, [[(-1, -1), 'B', True]]

def sendLaser(grid, start):
    touched = [[False for x in range(len(grid[0]))] for y in range(len(grid))]
    lasers = [start]
    allLasers = set()
    while True:
        if len(lasers) == 0:
            break
        laser = lasers[-1]
        lasers.pop()
        if not stringify(laser) in allLasers:
            touched, newLasers = laserize(grid, touched, laser[0], laser[1], laser[2])
            for newLaser in newLasers:
                if newLaser[1] != 'B':
                    allLasers.update({stringify(laser)})
                    lasers.append(newLaser)
        # print(lasers)
        # prettyPrint(touched, grid)
        # print()
    return touched

def part1(grid):
    touched = sendLaser(grid, [(0,0),'E', False])
    #prettyPrint(touched, grid)
    print(f"Part 1: {np.count_nonzero(np.asarray(touched))}")


def part2(data):
    ans = 0
    for i in range(len(data)):
        touched = sendLaser(data, [(0, i), 'S', False])
        ans = max(ans, np.count_nonzero(np.asarray(touched)))
        touched = sendLaser(data, [(len(data) - 1, i), 'N', False])
        ans = max(ans, np.count_nonzero(np.asarray(touched)))
    for i in range(len(data[0])):
        touched = sendLaser(data, [(i, 0), 'E', False])
        ans = max(ans, np.count_nonzero(np.asarray(touched)))
        touched = sendLaser(data, [(len(data[0])-1, i), 'W', False])
        ans = max(ans, np.count_nonzero(np.asarray(touched)))
    print(f"Part 2: {ans}")





if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    data = [list(x.replace('\n', '')) for x in open("day16.txt", "r").readlines()]
    #part1(data)
    part2(data)