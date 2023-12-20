import copy

import numpy as np


def parse():
    data= []
    for line in open("day18.txt", "r").readlines():
        d, n, c = line.replace("\n", '').split(' ')
        data.append([d, int(n), c[1:-1]])
    return data


def prettyPrint(ground):
    for gr in ground:
        for g in gr:
            print(g.ljust(2), end='')
        print()

def trim(ground):
    dug = []
    for row in ground:
        if row.count('#') != 0:
            dug.append(row)
    ldug = []
    for col in np.asarray(dug).T:
        if np.count_nonzero(col == '#') != 0:
            ldug.append(list(col))
    return list(np.asarray(ldug).T)

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

def fill(dug):
    oldPipes = copy.deepcopy(dug)
    changed = True
    while changed:
        for i in range(len(dug)):
            for j in range(len(dug[0])):
                if dug[i][j] == '.' and (onEdge(dug, i, j) or touchingEdge(dug, i, j)):
                    dug[i][j] = 'E'
        changed = not (np.array(dug) == np.array(oldPipes)).all()
        oldPipes = copy.deepcopy(dug)
    return dug




def part1_Slow(data):
    ground = [['.' for _ in range(10000)] for _ in range(10000)]
    x = y = 5000
    ground[x][y] = '#'
    for d,n,c in data:
        if d == 'U':
            for _ in range(n):
                x -= 1
                ground[x][y] = '#'
        if d == 'R':
            for _ in range(n):
                y += 1
                ground[x][y] = '#'
        if d == 'D':
            for _ in range(n):
                x += 1
                ground[x][y] = '#'
        if d == 'L':
            for _ in range(n):
                y -= 1
                ground[x][y] = '#'
    dug = trim(ground)
    dug = fill(dug)
    prettyPrint(dug)
    print(f"Part 1: {np.count_nonzero(np.logical_or(np.asarray(dug) == '#',np.asarray(dug) == '.'))}")

def part1(data):
    vertices = []
    xs = []
    ys = []
    x = y = 0
    for d, n, c in data:
        if d == 'U':
            x -= n
        if d == 'R':
            y += n
        if d == 'D':
            x += n
        if d == 'L':
            y -= n
        xs.append(x)
        ys.append(y)
    vertices = [[x - min(xs),y-min(ys)] for x,y in zip(xs, ys)]
    #print(vertices)
    area = 0
    perim = 0
    for i in range(len(vertices)):
        j = (i+1) % len(vertices)
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[i][1] * vertices[j][0]
        perim += abs(vertices[i][0] - vertices[j][0]) + abs(vertices[i][1] - vertices[j][1])
    #print(abs(area/2))
    print(f"Part 1 {perim/2 + abs(area/2) + 1}")


def part2(data):
    dirs = ['R', 'D', 'L', 'U']
    vertices = []
    xs = []
    ys = []
    x = y = 0
    for hexa in data:
        d = dirs[int(hexa[-1])]
        n = int(hexa[1:-1], 16)
        if d == 'U':
            x -= n
        if d == 'R':
            y += n
        if d == 'D':
            x += n
        if d == 'L':
            y -= n
        xs.append(x)
        ys.append(y)
    vertices = [[x - min(xs), y - min(ys)] for x, y in zip(xs, ys)]
    #print(vertices)
    area = 0
    perim = 0
    for i in range(len(vertices)):
        j = (i + 1) % len(vertices)
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[i][1] * vertices[j][0]
        perim += abs(vertices[i][0] - vertices[j][0]) + abs(vertices[i][1] - vertices[j][1])
    #print(abs(area / 2))
    print(f"Part 2 {perim / 2 + abs(area / 2) + 1}")

if __name__ == "__main__":
    data = parse()
    #part1_Slow(data)
    part1(data)
    data = [x[2] for x in data]
    part2(data)