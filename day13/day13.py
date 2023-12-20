import numpy as np


def parse():
    grid = []
    with open("day13.txt", "r") as f:
        mirrors = []
        for line in f.readlines():
            if line == '\n':
                grid.append(np.asarray(mirrors))
                mirrors = []
            else:
                line = line.replace('\n', '')
                mirrors.append(list(line))
        if len(mirrors) != 0:
            grid.append(np.asarray(mirrors))
    return grid

def checkRotation(x1, x2, mirrors):
    for i in range(min(x1, len(mirrors) - x2 - 1)):
        x1 -= 1
        x2 += 1
        if not np.equal(np.asarray(mirrors[x1]), np.asarray(mirrors[x2])).all():
            return False
    return True

def checkRotation2(x1, x2, mirrors, fixedSmudge):
    for i in range(min(x1, len(mirrors) - x2 - 1)):
        x1 -= 1
        x2 += 1
        same = np.equal(np.asarray(mirrors[x1]), np.asarray(mirrors[x2]))
        if same.tolist().count(False) == 1 and not fixedSmudge:
            fixedSmudge = True
        elif not np.equal(np.asarray(mirrors[x1]), np.asarray(mirrors[x2])).all():
            return False, fixedSmudge
    return True, fixedSmudge


def findRotation(mirrors):
    for i in range(len(mirrors) - 1):
        if np.equal(np.asarray(mirrors[i]), np.asarray(mirrors[i+1])).all()\
                and checkRotation(i, i+1, mirrors):
            return i + 1, i+2
    return -1, -1

def findRotation2(mirrors):
    for i in range(len(mirrors) - 1):
        same = np.equal(np.asarray(mirrors[i]), np.asarray(mirrors[i+1]))
        if same.all():
            reflect, smudged = checkRotation2(i, i+1, mirrors, False)
            if reflect and smudged:
                return i + 1, i+2
        elif same.tolist().count(False) == 1:
            reflect, _ = checkRotation2(i, i+1, mirrors, True)
            if reflect:
                return i + 1, i + 2
    return -1, -1


def part1(grid):
    ans = 0
    for i, mirrors in enumerate(grid):
        # print(f"Grid: {i + 1}")
        x1, x2 = findRotation(mirrors)
        y1, y2 = findRotation(mirrors.T)
        if x1 != x2 != -1:
            #print(f"X reflection {x1}, {x2}")
            ans += 100 * x1
        elif y1 != y2 != -1:
            #print(f"Y reflection {y1}, {y2}")
            ans += y1
    print(f"Part 1 = {ans}")

def part2(grid):
    ans = 0
    for i, mirrors in enumerate(grid):
        #print(f"Grid: {i + 1}")
        x1, x2 = findRotation2(mirrors)
        y1, y2 = findRotation2(mirrors.T)
        if x1 != x2 != -1:
            #print(f"Row reflection {x1}, {x2}")
            ans += 100 * x1
        elif y1 != y2 != -1:
            #print(f"Column reflection {y1}, {y2}")
            ans += y1
    print(f"Part 2 = {ans}")


if __name__ == '__main__':
    grid = parse()
    part1(grid)
    part2(grid)