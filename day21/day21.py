import copy
import math

import numpy as np

def hitsWall(garden, x, y):
    return x < 0 or y < 0 or x > len(garden) -1 or y > len(garden[0]) -1

def getAdj(garden, spot):
    sx, sy = spot
    steps =[]
    if not hitsWall(garden, sx-1, sy) and garden[sx-1][sy] != '#':
        steps.append((sx-1, sy))
    if not hitsWall(garden, sx+1, sy) and garden[sx+1][sy] != '#':
        steps.append((sx+1, sy))
    if not hitsWall(garden, sx, sy-1) and garden[sx][sy-1] != '#':
        steps.append((sx, sy-1))
    if not hitsWall(garden, sx, sy+1) and garden[sx][sy+1] != '#':
        steps.append((sx, sy+1))
    return steps

def prettyPrint(garden, spots):
    tGarden = copy.deepcopy(garden)
    for x, y in spots:
        tGarden[x][y] = 'O'
    for row in tGarden:
        for j in row:
            print(j, end=' ')
        print()

def part1(garden, start, numSteps):
    spots = set()
    spots.update({tuple(start)})
    for step in range(numSteps):
        stepped = set()
        for spot in spots:
            adjs = getAdj(garden, spot)
            stepped.update(adjs)
        spots = stepped
    #prettyPrint(garden, spots)
    return len(spots)


def getAdj2(garden, spot):
    sx, sy, v, h = spot
    steps =[]
    if garden[(sx+1) % len(garden)][sy] != '#':
        outx = sx+1 == len(garden)
        newv = v-1 if outx else v
        steps.append(((sx+1) % len(garden[0]), sy, newv, h))
    if garden[sx][(sy+1) % len(garden[0])] != '#':
        outy = sy + 1 == len(garden[0])
        newh = h+ 1 if outy else h
        steps.append((sx, (sy+1) % len(garden[0]), v,newh))
    negX = False
    if sx-1 == -1:
        sx = len(garden)
        negX = True
    if garden[sx - 1][sy] != '#':
        newv = v+1 if negX else v
        steps.append((sx - 1, sy, newv,h))
        if sx == len(garden):
            sx = 0
    negY = False
    if sy -1 == -1:
        sy = len(garden[0])
        negY = True
    if garden[sx][sy-1] != '#':
        newh = h - 1 if negY else h
        steps.append((sx, sy-1, v,newh))
    return steps

strides = 1
def part2(garden, s, numSteps):
    #numSteps = 130*strides+65
    spots = set()
    start = copy.deepcopy(s)
    start.extend([0,0])
    spots.update({tuple(start)})
    for step in range(numSteps):
        stepped = set()
        for spot in spots:
            adjs = getAdj2(garden, spot)
            stepped.update(adjs)
        spots = stepped
    # prettyPrint(garden, spots)
    # print()
    #print(spots)
    return len(spots)

def isOut(garden, i, j, s):
    sx, sy = s
    v = (len(garden)-1) // 2
    h = (len(garden[0])-1) // 2
    return abs(sx - i) + abs(sy - j) > v

def getParity(garden, s, steps):
    spots = set()
    start = copy.deepcopy(s)
    start.extend([0,0])
    spots.update({tuple(start)})
    for step in range(steps):
        stepped = set()
        for spot in spots:
            adjs = getAdj2(garden, spot)
            stepped.update(adjs)
        spots = stepped
    tGarden = copy.deepcopy(garden)
    for x, y, v, h in spots:
        if v == h == 0:
            tGarden[x][y] = 'O'
    return tGarden

def getOdd(garden, start):
    return part1(garden, start, 3 * len(garden) + 1)

def getEven(garden, start):
    return part1(garden, start, 3 * len(garden))


def getA(garden):
    s = (3 * len(garden) - 3) // 2
    tl = part1(garden, [0,0], s)
    tr = part1(garden,[0, len(garden[0])-1], s)
    bl = part1(garden, [len(garden)-1,0], s)
    br = part1(garden,[len(garden)-1, len(garden[0])-1], s)
    print(tl, tr, bl, br)
    return tl + tr + bl + br

def getB(garden):
    s = (len(garden) - 3) // 2
    tl = part1(garden, [0,0], s)
    tr = part1(garden,[0, len(garden[0])-1], s)
    bl = part1(garden, [len(garden)-1,0], s)
    br = part1(garden,[len(garden)-1, len(garden[0])-1], s)
    print(tl, tr, bl, br)
    return tl + tr + bl + br

def getT(garden):
    s = len(garden)
    s0 = (len(garden) - 1) // 2
    tl = part1(garden, [0,s0], s)
    tr = part1(garden,[s0, 0], s)
    bl = part1(garden, [len(garden)-1,s0], s)
    br = part1(garden,[s0, len(garden[0])-1], s)
    print(tl, tr, bl, br)
    return tl + tr + bl + br

def part2_working(garden, s):
    # evenFull = 0
    # oddFull = 0
    # oddOut = 0
    # evenOut = 0
    # print("even")
    # for i, gar in enumerate(getParity(garden,s, 130)):
    #     for j, g in enumerate(gar):
    #         if g == 'O':
    #             evenFull += 1
    #             if isOut(garden, i, j, s):
    #                 evenOut += 1
    #     #     print(g, end="")
    #     # print()
    # print("odd")
    # for i, gar in enumerate(getParity(garden,s, 131)):
    #     for j, g in enumerate(gar):
    #         if g == 'O':
    #             oddFull += 1
    #             if isOut(garden, i, j, s):
    #                 oddOut += 1
    #     #     print(g, end="")
    #     # print()
    # print(evenFull, oddFull)
    # print(evenOut, oddOut)


    steps = 26501365
    n = (steps -65) // 131
    o = getOdd(garden,s)
    e = getEven(garden,s)
    a = getA(garden)
    b = getB(garden)
    t = getT(garden)
    print(e, o, a, b, t)
    full = (((n-1)**2) * o) + ((n**2) * e) + ((n-1) * a) + (n * b) + t
    print(full)

    # n = steps // len(garden)
    # The elf starts in the center of the grid
    a = part1(garden, s)
    a, b, c = (
        part1(garden, s, x * len(garden) + (len(garden) // 2))
        for x in range(3)
    )
    # NOTE: This part of my solution comes verbatim from someone else.
    # (No, I won't explain it. No, I'm not sorry.)
    print( a + n * (b - a + (n - 1) * (c - b - b + a) // 2))
    # full = (n**2) * oddFull + (n-1)**2 * evenFull - ((n) * oddOut) + (n-1) * evenOut
    # print("odd", full)
    # full = ((n ** 2) * evenFull) + (((n - 1) ** 2) * oddFull) - (n * evenOut) + ((n - 1) * oddOut)
    # print("even", full)

def part2AAAAAA(garden, s):
    n= 26501365 // 131
    a = part2(garden, s, 65)
    print(a)
    b = part2(garden, s, 65+(131*1))
    print(b)
    c = part2(garden, s, 65+(131*2))
    print(c)
    print(a+n*(b-a+(n-1)*(c-b-b+a)//2))



if __name__ == "__main__":
    data = [list(line.replace('\n', '')) for line in open("day21.txt", "r").readlines()]
    s = np.argwhere(np.array(data) == 'S')[0]
    # part1(data, s, 64)
    #part2(data, list(s))
    part2AAAAAA(data, list(s))





# def part2_working(garden, s):
#     evenFull = 0
#     oddFull = 0
#     oddOut = 0
#     evenOut = 0
#     print("even")
#     for i, gar in enumerate(getParity(garden,s, 130)):
#         for j, g in enumerate(gar):
#             if g == 'O':
#                 evenFull += 1
#                 if isOut(garden, i, j, s):
#                     evenOut += 1
#             print(g, end="")
#         print()
#     print("odd")
#     for i, gar in enumerate(getParity(garden,s, 131)):
#         for j, g in enumerate(gar):
#             if g == 'O':
#                 oddFull += 1
#                 if isOut(garden, i, j, s):
#                     oddOut += 1
#             print(g, end="")
#         print()
#     print(evenFull, oddFull)
#     print(evenOut, oddOut)
#     steps = 26501365
#     n = (steps -65) // 131
#     print(n)
#     full = (n**2) * oddFull + (n-1)**2 * evenFull - ((n) * oddOut) + (n-1) * evenOut
#     print("odd", full)
#     full = ((n ** 2) * evenFull) + (((n - 1) ** 2) * oddFull) - (n * evenOut) + ((n - 1) * oddOut)
#     print("even", full)

