import copy
import math
import time


def hitsWall(grid, x,y):
    return x < 0 or y < 0 or x > len(grid) -1 or y > len(grid[0]) - 1

def prettyPrint(grid):
    for row in grid:
        for col in row:
            print(str(col).ljust(5), end= '')
        print()
    print()

def getAdjs(trail, x,y, d):
    adjs = []
    if trail[x][y] == '>':
        adjs.append((x, y+1, 'E'))
        return adjs
    if trail[x][y] == '<':
        adjs.append((x, y-1, 'W'))
        return adjs
    if trail[x][y] == '^':
        adjs.append((x-1, y, 'N'))
        return adjs
    if trail[x][y] == 'v':
        adjs.append((x+1, y, 'S'))
        return adjs
    if not hitsWall(trail, x-1, y) and trail[x-1][y] != '#' and trail[x-1][y] != 'v' and d != 'S':
        adjs.append((x-1, y, 'N'))
    if not hitsWall(trail, x+1, y) and trail[x+1][y] != '#' and trail[x+1][y] != '^' and d != 'N':
        adjs.append((x+1, y, 'S'))
    if not hitsWall(trail, x, y-1) and trail[x][y-1] != '#' and trail[x][y-1] != '>' and d != 'E':
        adjs.append((x, y-1, 'W'))
    if not hitsWall(trail, x, y+1) and trail[x][y+1] != '#' and trail[x][y+1] != '<' and d != 'W':
        adjs.append((x, y+1, 'E'))
    return adjs

def inQueue(queue, node):
    nx, ny, d = node
    for i,(w,x,y, d, vis) in enumerate(queue):
        if x == nx and ny == y:
            return w, x, y, d, i
    return math.inf, nx, ny, 'A', -1

def trailblaze(trails):
    weights = copy.deepcopy(trails)
    for i, row in enumerate(weights):
        for j, c in enumerate(row):
            if c != '#':
                weights[i][j] = math.inf
    #prettyPrint(trails)
    queue = [(0, 1, 0, 'S')]
    # weight, x, y, direction
    while queue:
        queue = sorted(queue, key=lambda z: z[0])
        w, x, y, d = queue.pop()
        if x == len(trails) -1 and y == len(trails[0]) - 2:
            continue
        adjs = getAdjs(trails, x,y, d)
        for adj in adjs:
            qw, ax, ay, _, ind = inQueue(queue, adj)
            aw = w-1
            ad = adj[2]
            if aw == -77:
                pass
            if ind != -1 and aw < qw:
                queue[ind] = (aw, ax, ay, ad)
                weights[ax][ay] = aw
            elif aw < qw:
                weights[ax][ay] = aw
                queue.append((aw, ax, ay, ad))
    #     prettyPrint(weights)
    # prettyPrint(weights)
    return weights

def getAdjs2(trail, x,y, d):
    adjs = []
    if not hitsWall(trail, x-1, y) and trail[x-1][y] != '#' and d != 'S':
        adjs.append((x-1, y, 'N'))
    if not hitsWall(trail, x+1, y) and trail[x+1][y] != '#' and d != 'N':
        adjs.append((x+1, y, 'S'))
    if not hitsWall(trail, x, y-1) and trail[x][y-1] != '#' and d != 'E':
        adjs.append((x, y-1, 'W'))
    if not hitsWall(trail, x, y+1) and trail[x][y+1] != '#' and d != 'W':
        adjs.append((x, y+1, 'E'))
    return adjs

def trailblaze2(trails):
    weights = copy.deepcopy(trails)
    for i, row in enumerate(weights):
        for j, c in enumerate(row):
            if c != '#':
                weights[i][j] = math.inf
    #prettyPrint(trails)
    queue = [(0, 1, 0, 'S', {(0,1)})]

    # weight, x, y, direction
    while queue:
        print(len(queue))
        queue = sorted(queue, key=lambda z: z[0])
        w, x, y, d, visited = queue.pop()
        if x == len(trails) -1 and y == len(trails[0]) - 2:
            continue
        adjs = getAdjs2(trails, x,y, d)
        for adj in adjs:
            if (adj[0],adj[1]) in visited:
                continue
            qw, ax, ay, _, ind = inQueue(queue, adj)
            aw = w-1
            ad = adj[2]
            if aw == -77:
                pass
            aVis = copy.deepcopy(visited)
            aVis.update({(ax, ay)})
            if ind != -1:
                queue[ind] = (aw, ax, ay, ad,aVis)
                weights[ax][ay] = aw
            elif aw < qw:
                weights[ax][ay] = aw
                queue.append((aw, ax, ay, ad, aVis))
    #     prettyPrint(weights)
    # prettyPrint(weights)
    return weights

def part1(trail):
    weights = trailblaze(trail)
    print(f"Part 1: {-weights[len(weights) - 1][len(weights[0]) - 2]}")

def part2(trail):
    weights = trailblaze2(trail)
    print(f"Part 2: {-weights[len(weights) - 1][len(weights[0]) - 2]}")

if __name__ == "__main__":
    data = [list(line.replace('\n', '')) for line in open("day23.txt", "r").readlines()]
    #part1(data)
    part2(data)