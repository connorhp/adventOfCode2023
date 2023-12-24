import copy
import time


def hitsWall(grid, x,y):
    return x < 0 or y < 0 or x > len(grid) -1 or y > len(grid[0]) - 1

def getAdjs2(trail, x,y, seen, d):
    adjs = []
    if len(seen) == 1:
        if d == 'N':
            adjs.append(((x - 1, y), 'N'))
        elif d == 'S':
            adjs.append(((x + 1, y), 'S'))
        elif d == 'E':
            adjs.append(((x, y + 1), 'E'))
        elif d== 'W':
            adjs.append(((x, y - 1), 'W'))
        return adjs
    if not hitsWall(trail, x-1, y) and trail[x-1][y] != '#' and (x-1,y) not in seen:
        adjs.append(((x-1, y), 'N'))
    if not hitsWall(trail, x+1, y) and trail[x+1][y] != '#' and (x+1,y) not in seen:
        adjs.append(((x+1, y), 'S'))
    if not hitsWall(trail, x, y-1) and trail[x][y-1] != '#' and (x,y-1) not in seen:
        adjs.append(((x, y-1), 'W'))
    if not hitsWall(trail, x, y+1) and trail[x][y+1] != '#' and (x,y+1) not in seen:
        adjs.append(((x, y+1),'E'))
    return adjs

def flip(dir):
    ind = "NSEW".index(dir)
    return "SNWE"[ind]

def getNodes(trail):
    visited = set()
    nodes = {}
    queue = [((0,1), 'S')]
    while queue:
        fro, OGdire = queue.pop()
        if (fro, OGdire) in visited:
            continue
        visited.update({(fro, OGdire)})
        distFrom = 0
        curr = fro
        seen = set()
        while True:
            seen.add(curr)
            adjs = getAdjs2(trail, curr[0], curr[1], seen, OGdire)
            if len(adjs) > 1 or curr == (len(trail)-1,len(trail[0])-2):
                if fro not in nodes:
                    nodes[fro] = []
                nodes[fro].append((curr, distFrom))
                if curr not in nodes:
                    nodes[curr] = []
                nodes[curr].append((fro, distFrom))
                visited.add((curr, flip(OGdire)))
                for _, d in adjs:
                    if (curr, d) not in visited:
                        queue.append((curr, d))
                break
            elif len(adjs) == 1:
                curr = adjs[0][0]
                distFrom += 1
    return nodes

def trailblaze(nodes, node, dist, best, seen, stop):
    if node == stop:
        #print(dist)
        return dist
    if node in seen:
        return best
    seen.update({node})
    bests = [trailblaze(nodes, n, d + dist,best, seen, stop) for n, d in nodes[node]]
    seen.remove(node)
    return max(bests)

def part2(trail):
    nodes = getNodes(trail)
    st = time.perf_counter()
    print(trailblaze(nodes, (0,1), 0, 0, set(), (len(trail)-1, len(trail[0])-2)))
    print(f"Part 2: in {time.perf_counter() - st:.2f} seconds")

if __name__ == "__main__":
    data = [list(line.replace('\n', '')) for line in open("day23.txt", "r").readlines()]
    #part1(data)
    part2(data)