import math
import sys
import numpy as np
import copy

startx = -1
starty = -1

def parse():
    with open("day10.txt", "r") as f:
        global startx
        global starty
        pipes = []
        for i, line in enumerate(f.readlines()):
            line = line.replace('\n', '')
            line = line.replace(' ','')
            pipes.append(list(line))
        return pipes

def getSConnections(pipes):
    global startx
    global starty
    for i in range(len(pipes)):
        for j in range(len(pipes[0])):
            if pipes[i][j] == 'S':
                    startx = i
                    starty = j
    x = startx
    y = starty

    sConns = []
    if x != 0 and up(pipes[x - 1][y], "UP"):
        sConns.append([x-1, y])
    if x != len(pipes)-1 and down(pipes[x + 1][y], "DOWN"):
        sConns.append([x+1, y])
    if y != 0 and left(pipes[x][y - 1], "LEFT"):
        sConns.append([x, y-1])
    if y != len(pipes[0])-1 and right(pipes[x][y + 1], "RIGHT"):
        sConns.append([x, y+1])
    return sConns

def up(to, dir):
    return (to == '7' or to == 'F' or to == '|') and dir == "UP"

def down(to, dir):
    return (to == 'L' or to == 'J' or to == '|') and dir == "DOWN"

def left(to, dir):
    return (to == 'L' or to == 'F' or to == '-') and dir == "LEFT"

def right(to, dir):
    return (to == '7' or to == 'J' or to == '-') and dir == "RIGHT"


def canConnect(where,to, dir):
    if to == 'S' or to == '.':
        return False
    if where == '|':
        return up(to, dir) or down(to, dir)
    elif where == '-':
        return left(to, dir) or right(to, dir)
    elif where == 'L':
        return up(to, dir) or right(to, dir)
    elif where == 'J':
        return up(to, dir) or left(to, dir)
    elif where == '7':
        return down(to, dir) or left(to, dir)
    elif where == 'F':
        return down(to, dir) or right(to, dir)
    return False

def pipe(pipes, distances, x, y, dis, used):
    while True:
        used[x][y] = True
        distances[x][y] = min(distances[x][y], dis)
        where = pipes[x][y]
        if x != 0 and canConnect(pipes[x][y], pipes[x-1][y], "UP") and not used[x-1][y]:
            #print(f"{where} UP {pipes[x-1][y]}, {x}, {y}, {dis}")
            x -= 1
        elif x != len(pipes)-1 and canConnect(pipes[x][y], pipes[x+1][y], "DOWN") and not used[x+1][y]:
            #print(f"{where} DOWN {pipes[x + 1][y]}, {x}, {y}, {dis}")
            x += 1
        elif y != 0 and canConnect(pipes[x][y], pipes[x][y-1], "LEFT") and not used[x][y-1]:
            #print(f"{where} LEFT {pipes[x][y-1]}, {x}, {y}, {dis}")
            y-=1
        elif y != len(pipes[0])-1 and canConnect(pipes[x][y], pipes[x][y+1], "RIGHT") and not used[x][y+1]:
            #print(f"{where} RIGHT {pipes[x][y+1]}, {x}, {y}, {dis}")
            y+=1
        else:
            break
        dis+=1
    return distances


def onEdge(pipes, i, j):
    return i == 0 or j == 0 or i == len(pipes) -1 or j == len(pipes[0]) - 1

def touchingEdge(pipes, i, j):
    if i != 0 and pipes[i-1][j] == 'E':
        return True
    if i != len(pipes) - 1 and pipes[i+1][j] == 'E':
        return True
    if j != 0 and pipes[i][j-1] == 'E':
        return True
    if j != len(pipes[0]) - 1 and pipes[i][j+1] == 'E':
        return True
    return False

def findEnclosed(pipes):
    oldPipes = copy.deepcopy(pipes)
    changed = True
    while changed:
        for i in range(len(pipes)):
            for j in range(len(pipes[0])):
                if pipes[i][j] == '.' and (onEdge(pipes, i, j) or touchingEdge(pipes, i, j)):
                    pipes[i][j] = 'E'
        changed = not (np.array(pipes) == np.array(oldPipes)).all()
        oldPipes = copy.deepcopy(pipes)
    return pipes

def printStuff(distances, pipes, added):
    for i in range(len(pipes)):
        for j in range(len(pipes[0])):
            if math.isinf(distances[i][j]):
                distances[i][j] = -1

                pipes[i][j] = '.'
            #print(f"{int(distances[i][j])} " , end='')
            print(f"{pipes[i][j]} ", end='')
        print()


def doublePipes(pipes):
    added = []
    pipes2 = []
    for pipeLine in pipes:
        pipeLine2 = []
        addedLine = []
        for pipe in pipeLine:
            pipeLine2.append(pipe)
            pipeLine2.append('-')
            addedLine.append(False)
            addedLine.append(True)
        pipes2.append(pipeLine2)
        added.append(addedLine)
        pipes2.append(['|' for x in range(len(pipeLine2))])
        added.append([True for x in range(len(pipeLine2))])
    return pipes2, added

def part2(pipes):
    pipes, added = doublePipes(pipes)

    distances = np.full((len(pipes), len(pipes[0])), math.inf)
    distances[startx][starty] = 0
    sConns = getSConnections(pipes)
    for sConn in sConns:
        used = np.full((len(pipes), len(pipes[0])), False)
        distances = pipe(pipes, distances, sConn[0], sConn[1], 1, used)
    printStuff(distances, pipes, added)
    pipes = findEnclosed(pipes)
    ans = -1
    for i in range(len(pipes)):
        for j in range(len(pipes[0])):
            if pipes[i][j] == '.' and not added[i][j]:
                pipes[i][j] = 'I'
                ans += 1
    printStuff(distances, pipes, added)
    print(ans)



def part1(pipes):
    distances = np.full((len(pipes), len(pipes[0])), math.inf)
    distances[startx][starty] = 0
    sConns = getSConnections(pipes)
    for sConn in sConns:
        used = np.full((len(pipes), len(pipes[0])), False)
        distances = pipe(pipes, distances, sConn[0], sConn[1], 1, used)
    printStuff(distances, pipes)
    print(f"Part 1: {np.amax(distances)}")

if __name__ == '__main__':
    #sys.setrecursionlimit(2500)
    pipes = parse()
    #part1(pipes)
    part2(pipes)
