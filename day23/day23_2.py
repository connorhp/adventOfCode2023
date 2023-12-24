import copy
import math
import sys


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

def getAdjs2(trail, x,y, seen):
    adjs = []
    if not hitsWall(trail, x-1, y) and trail[x-1][y] != '#' and (x-1,y) not in seen:
        adjs.append((x-1, y))
    if not hitsWall(trail, x+1, y) and trail[x+1][y] != '#' and (x+1,y) not in seen:
        adjs.append((x+1, y))
    if not hitsWall(trail, x, y-1) and trail[x][y-1] != '#' and (x,y-1) not in seen:
        adjs.append((x, y-1))
    if not hitsWall(trail, x, y+1) and trail[x][y+1] != '#' and (x,y+1) not in seen:
        adjs.append((x, y+1))
    return adjs


def trailblaze2(trails, node, dist, best, seen):
    seen.update({node})
    prev = node
    while True:
        if prev == (len(trails) - 1, len(trails[0]) - 2):
            print(dist)
            return dist
        adjs = getAdjs2(trails, prev[0], prev[1], seen)
        if len(adjs) >= 2:
            bests = [best]
            for adj in adjs:
                bests.append(trailblaze2(trails, adj, dist + 1, best, copy.deepcopy(seen)))
            return max(bests)
        elif len(adjs) == 0:
            return best
        else:
            prev = adjs[0]
            seen.update({prev})
            dist+=1


def part1(trail):
    weights = trailblaze(trail)
    print(f"Part 1: {-weights[len(weights) - 1][len(weights[0]) - 2]}")

def part2(trail):

    print(f"Part 2: {trailblaze2(trail, (0,1), 0, 0, {(0,1)})}")

if __name__ == "__main__":
    sys.setrecursionlimit(4000)
    data = [list(line.replace('\n', '')) for line in open("day23.txt", "r").readlines()]
    #part1(data)
    part2(data)