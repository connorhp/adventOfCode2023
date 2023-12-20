import math
import time


def getAns(grid, nodes, part):
    last = []
    if part == 1:
        last = [node for node in nodes if node[1] == len(grid)-1 and node[2] == len(grid[0])-1]
    if part == 2:
        last = [node for node in nodes if node[1] == len(grid) - 1 and node[2] == len(grid[0]) - 1 and node[4] >= 4]
    return sorted(last, key=lambda z: (z[0]))[0]

def hitsWall(grid, x,y):
    return x < 0 or y < 0 or x > len(grid) -1 or y > len(grid[0]) - 1

def getAdj1(traveled, x, y, d, dis):
    adj = []
    dis = int(dis)
    masDis = 3
    if x == y == 0:
        if not hitsWall(traveled, x-1, y):
            adj.append((x-1, y, 'N', 1))
        if not hitsWall(traveled,x, y+1):
            adj.append((x, y+1, 'E', 1))
        if not hitsWall(traveled,x, y -1):
            adj.append((x, y -1, 'W', 1))
        if not hitsWall(traveled, x + 1, y):
            adj.append((x+1, y, 'S', 1))
    elif d == 'N':
        if dis < masDis and not hitsWall(traveled, x-1, y):
            adj.append((x-1, y, 'N', dis+1))
        if not hitsWall(traveled,x, y+1):
            adj.append((x, y+1, 'E', 1))
        if not hitsWall(traveled,x, y -1):
            adj.append((x, y -1, 'W', 1))
    elif d == 'S':
        if dis < masDis and not hitsWall(traveled,x + 1, y):
            adj.append((x + 1, y, 'S', dis + 1))
        if not hitsWall(traveled,x, y + 1):
            adj.append((x, y + 1, 'E', 1))
        if not hitsWall(traveled, x, y - 1):
            adj.append((x, y - 1, 'W', 1))
    elif d == 'E':
        if dis < masDis and not hitsWall(traveled, x, y+1):
            adj.append((x, y+1, 'E', dis + 1))
        if not hitsWall(traveled, x - 1, y):
            adj.append((x-1, y, 'N', 1))
        if not hitsWall(traveled, x + 1, y):
            adj.append((x+1, y, 'S', 1))
    elif d == 'W':
        if dis < masDis and not hitsWall(traveled, x, y-1):
            adj.append((x, y-1, 'W', dis + 1))
        if not hitsWall(traveled, x-1, y):
            adj.append((x-1, y, 'N', 1))
        if not hitsWall(traveled, x + 1, y):
            adj.append((x+1, y, 'S', 1))
    return adj

def getAdj2(traveled, x, y, d, dis):
    adj = []
    dis = int(dis)
    masDis = 10
    if x == y == 0:
        if not hitsWall(traveled, x-1, y):
            adj.append((x-1, y, 'N', 1))
        if not hitsWall(traveled,x, y+1):
            adj.append((x, y+1, 'E', 1))
        if not hitsWall(traveled,x, y -1):
            adj.append((x, y -1, 'W', 1))
        if not hitsWall(traveled, x + 1, y):
            adj.append((x+1, y, 'S', 1))
    elif dis < 4:
        if d == 'N' and not hitsWall(traveled, x-1, y):
            adj.append((x-1,y, d, dis+1))
        elif d == 'S' and not hitsWall(traveled, x+1, y):
            adj.append((x+1,y, d, dis+1))
        elif d == 'E' and not hitsWall(traveled, x, y+1):
            adj.append((x,y+1, d, dis+1))
        elif d == 'W' and not hitsWall(traveled, x, y-1):
            adj.append((x,y-1, d, dis+1))
    elif d == 'N':
        if dis < masDis and not hitsWall(traveled, x - 1, y):
            adj.append((x - 1, y, 'N', dis + 1))
        if not hitsWall(traveled, x, y + 1):
            adj.append((x, y + 1, 'E', 1))
        if not hitsWall(traveled, x, y - 1):
            adj.append((x, y - 1, 'W', 1))
    elif d == 'S':
        if dis < masDis and not hitsWall(traveled, x + 1, y):
            adj.append((x + 1, y, 'S', dis + 1))
        if not hitsWall(traveled, x, y + 1):
            adj.append((x, y + 1, 'E', 1))
        if not hitsWall(traveled, x, y - 1):
            adj.append((x, y - 1, 'W', 1))
    elif d == 'E':
        if dis < masDis and not hitsWall(traveled, x, y + 1):
            adj.append((x, y + 1, 'E', dis + 1))
        if not hitsWall(traveled, x - 1, y):
            adj.append((x - 1, y, 'N', 1))
        if not hitsWall(traveled, x + 1, y):
            adj.append((x + 1, y, 'S', 1))
    elif d == 'W':
        if dis < masDis and not hitsWall(traveled, x, y - 1):
            adj.append((x, y - 1, 'W', dis + 1))
        if not hitsWall(traveled, x - 1, y):
            adj.append((x - 1, y, 'N', 1))
        if not hitsWall(traveled, x + 1, y):
            adj.append((x + 1, y, 'S', 1))
    return adj




def inQueue(queue, node):
    nx, ny, ndir, ndis = node
    for i,(w,x,y,direct,dis) in enumerate(queue):
        if x == nx and ny == y and ndir == direct and ndis == dis:
            return w, x, y, direct, dis, i
    return math.inf, nx, ny, ndir, ndis, -1

def inNodes(nodes, node):
    nx, ny, ndir, ndis = node
    for i, (w, x, y, direct, dis) in enumerate(nodes):
        if x == nx and ny == y and ndir == direct and ndis == dis:
            return i
    return -1

def path(grid, part):
    start = time.perf_counter()
    nodes = []
    visited = set()
    queue = []
    # weight, x, y, direction, distance
    queue.append((0, 0,0, 'A', 1))
    nodes.append((0, 0,0, 'A', 1))

    while queue:
        queue = sorted(queue, key=lambda z: z[0], reverse=True)
        w,x,y,direct, dist = queue[-1]
        queue.pop()
        adjs = []
        if part == 1:
            adjs = getAdj1(grid, x, y, direct, dist)
        elif part == 2:
            adjs = getAdj2(grid, x, y, direct, dist)
        for adj in adjs:
            if adj in visited:
                continue
            qw, ax, ay, adir, adis, ind = inQueue(queue, adj)
            aw = grid[ax][ay] + w
            if ind != -1:
                if aw < qw:
                    queue[ind] = (aw, ax, ay, adir, adis)
                    nodes[inNodes(nodes, adj)] = (aw, ax, ay, adir, adis)
            else:
                queue.append((aw, ax, ay, adir, adis))
                nodes.append((aw, ax, ay, adir, adis))
        visited.add((x,y,direct, dist))
    # nodes = sorted(nodes, key=lambda z: (z[1], z[2], z[1]))
    # for node in nodes:
    #     print(node)
    print(f"Part {part}: {getAns(grid, nodes, part)[0]} in {(time.perf_counter() - start):0.2f} seconds")



if __name__ == "__main__":
    data = [list(int(y) for y in list(x.replace('\n', ''))) for x in open("day17.txt", "r").readlines()]
    data[0][0] = 0
    path(data, 2)