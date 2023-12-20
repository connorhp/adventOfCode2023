import math

def prettyPrint(traveled):
    for tra in traveled:
        for t in tra:
            print(str(t).ljust(5), end='')
        print()

def printPath(grid, path, startx, starty):
    x = startx
    y = starty
    while True:
        grid[x][y] = True
        if (x,y) not in path:
            break
        node = path.get((x,y))
        x,y = node
    #print(path.get((1,1)))
    #prettyPrint(grid)
    for tra in grid:
        for t in tra:
            if t:
                print('#'.ljust(2), end='')
            else:
                print('.'.ljust(2), end='')
        print()



def hitsWall(traveled, x,y):
    return x < 0 or y < 0 or x > len(traveled) -1 or y > len(traveled[0]) - 1

def getAdj2(traveled, x, y, d, dis):
    adj = []
    dis = int(dis)
    masDis = 3
    if x == y == 0:
        if not hitsWall(traveled, x-1, y):
            adj.append([x-1, y, 'N', 1])
        if not hitsWall(traveled,x, y+1):
            adj.append([x, y+1, 'E', 1])
        if not hitsWall(traveled,x, y -1):
            adj.append([x, y -1, 'W', 1])
        if not hitsWall(traveled, x + 1, y):
            adj.append([x+1, y, 'S', 1])
    elif d == 'N':
        if dis < masDis and not hitsWall(traveled, x-1, y):
            adj.append([x-1, y, 'N', dis+1])
        if not hitsWall(traveled,x, y+1):
            adj.append([x, y+1, 'E', 1])
        if not hitsWall(traveled,x, y -1):
            adj.append([x, y -1, 'W', 1])
    elif d == 'S':
        if dis < masDis and not hitsWall(traveled,x + 1, y):
            adj.append([x + 1, y, 'S', dis + 1])
        if not hitsWall(traveled,x, y + 1):
            adj.append([x, y + 1, 'E', 1])
        if not hitsWall(traveled, x, y - 1):
            adj.append([x, y - 1, 'W', 1])
    elif d == 'E':
        if dis < masDis and not hitsWall(traveled, x, y+1):
            adj.append([x, y+1, 'E', dis + 1])
        if not hitsWall(traveled, x - 1, y):
            adj.append([x-1, y, 'N', 1])
        if not hitsWall(traveled, x + 1, y):
            adj.append([x+1, y, 'S', 1])
    elif d == 'W':
        if dis < masDis and not hitsWall(traveled, x, y-1):
            adj.append([x, y-1, 'W', dis + 1])
        if not hitsWall(traveled, x-1, y):
            adj.append([x-1, y, 'N', 1])
        if not hitsWall(traveled, x + 1, y):
            adj.append([x+1, y, 'S', 1])
    return adj


def getAdj(traveled, x,y, links):
    if (x,y) in links:
        lx, ly = links.get((x,y))
    else:
        lx,ly = x,y
    adj = []
    if lx == x:
        if not hitsWall(traveled, x - 1, y):
            adj.append((x - 1, y, 1))
        if not hitsWall(traveled, x + 1, y):
            adj.append((x + 1, y, 1))
        if not hitsWall(traveled, x - 2, y):
            adj.append((x - 2, y, 2))
        if not hitsWall(traveled, x + 2, y):
            adj.append((x + 2, y, 2))
        if not hitsWall(traveled, x - 3, y):
            adj.append((x - 3, y, 3))
        if not hitsWall(traveled, x + 3, y):
            adj.append((x + 3, y, 3))
    if ly == y:
        if not hitsWall(traveled, x, y- 1):
            adj.append((x, y - 1, 1))
        if not hitsWall(traveled, x, y + 1):
            adj.append((x , y+1, 1))
        if not hitsWall(traveled, x , y- 2):
            adj.append((x, y - 2, 2))
        if not hitsWall(traveled, x, y + 2):
            adj.append((x, y + 2, 2))
        if not hitsWall(traveled, x , y- 3):
            adj.append((x, y- 3, 3 ))
        if not hitsWall(traveled, x , y+ 3):
            adj.append((x , y+ 3, 3))

    return adj

def getConnected(travel, x, y, links):
    con = []
    if (x,y) not in links:
        return getAdj(travel, x, y, links)
    px, py = links.get((x,y))
    if px == x:
        if not hitsWall(travel, x-1, y):
            con.append((x-1,y))
        if not hitsWall(travel, x+1, y):
            con.append((x+1,y))
        xs, ys = getPast(links, x,y)
        if xs.count(px) != 3:
            if not hitsWall(travel, x, y-1):
                con.append((x, y-1))
            if not hitsWall(travel, x, y+1):
                con.append((x, y+1))
    elif py == y:
        if not hitsWall(travel, x, y-1):
            con.append((x,y-1))
        if not hitsWall(travel, x, y+1):
            con.append((x,y+1))
        xs, ys = getPast(links, x,y)
        if ys.count(py) != 3:
            if not hitsWall(travel, x-1, y):
                con.append((x-1, y))
            if not hitsWall(travel, x+1, y):
                con.append((x+1, y))
    return con

def getPast(links, x,y):
    xs = []
    ys = []
    prevx = x
    prevy = y
    back = 4
    for _ in range(back):
        if (prevx, prevy) in links:
            xs.append(prevx)
            ys.append(prevy)
            prev = links.get((prevx, prevy))
            prevx, prevy = prev
    return xs, ys


def findInQueue(queue, x,y, d, dis):
    for i, (q, (ax, ay), ad, adis) in enumerate(queue):
        if ax == x and ay == y and ad == d and adis == dis:
            return i
    return -1

def mapBack(links, ax, ay, x, y):
    xs = [ax]
    ys = [ay]
    prevx = x
    prevy = y
    back = 3
    for _ in range(back):
        if (prevx, prevy) in links:
            xs.append(prevx)
            ys.append(prevy)
            prev = links.get((prevx, prevy))
            prevx, prevy = prev
    return xs.count(xs[0]) > back or ys.count(ys[0]) > back

def findPath(grid, traveled, x,y):
    visited = [[False for x in range(len(grid[0]))] for y in range(len(grid))]
    queue = []
    linked = {}
    traveled[x][y] = 0
    for i in range(len(traveled)):
        for j in range(len(traveled[0])):
            queue.append((traveled[i][j], (i,j), 'E', 0))
    #print(queue)

    traveled[x][y] = grid[x][y]
    while len(queue) != 0:
        queue = sorted(queue, key=lambda z: z[0], reverse=True)
        node = queue[-1]
        queue.pop()
        visited[x][y] = True
        _, (x,y), d, dis = node
        cost = traveled[x][y]
        adjs = getAdj2(traveled, x,y,d,dis)
        if x == 1 and y == 4:
            print()
        for adj in adjs:
            ax, ay, ad, adis = adj
            if visited[ax][ay]:
                continue
            s = grid[ax][ay]
            newWeight = cost + s
            if newWeight not in queue:
                queue.append((newWeight, (ax, ay), ad, adis))
            if traveled[ax][ay] > cost + s:
                linked.update({(ax,ay): (x,y)})
                traveled[ax][ay] = newWeight
                ind = findInQueue(queue, ax, ay, ad, adis)
                if ind != -1:
                    queue[ind] = (newWeight, (ax,ay), ad, adis)



        prettyPrint(traveled)
        print()
    return traveled, linked



def part1(grid):

    traveled = [[math.inf for x in range(len(grid[0]))] for y in range(len(grid))]
    grid[0][0] = 0
    #grid[len(grid)-1][len(grid[0])-1] = 0
    startx = 0
    starty = 0
    traveled, path = findPath(grid, traveled, startx, starty)
    prettyPrint(traveled)
    allPath = [[False for x in range(len(grid[0]))] for y in range(len(grid))]
    printPath(allPath, path, len(grid)-1 - startx, len(grid[0]) - 1 - starty)
    print(f"Part 1 {traveled[len(grid)-1 - startx][len(grid[0]) - 1 - starty]}")




if __name__ == "__main__":
    data = [list(int(y) for y in list(x.replace('\n', ''))) for x in open("day17.txt", "r").readlines()]
    part1(data)