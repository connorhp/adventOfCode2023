import numpy as np

def parse():
    with open("day11.txt", "r") as f:
        space = []
        for line in f.readlines():
            line = line.replace('\n','')
            space.append(list(line))
        return space

def expandSpace(space):
    expandedSpaces = []
    for i,line in enumerate(space):
        if not np.any(line == '#'):
            expandedSpaces.append(i)
    return np.array(expandedSpaces)


def findGalaxies(space):
    galaxies = []
    for i, line in enumerate(space):
        for j, spot in enumerate(line):
            if spot == '#':
                galaxies.append([i,j])
    return np.array(galaxies)

def getNumPassed(c1, c2, lines):
    passed = 0
    for line in lines:
        if c1 < line < c2:
            passed += 1
    return passed


def getDistances(galaxies, rows, cols, amount):
    ans = np.float16(0)
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            x1, y1 = galaxies[i]
            x2, y2 = galaxies[j]
            d = abs(y2 - y1) + abs(x2 - x1)
            numPassed = getNumPassed(min(y1, y2), max(y1, y2), cols) +  getNumPassed(min(x1, x2), max(x1, x2), rows)
            d += amount * numPassed - numPassed
            #print(f"{i+1} -> {j+1} = {d}: {numPassed}")
            ans = np.add(ans, d)
    return ans

if __name__ == '__main__':
    space = parse()
    space = np.array(space)
    expandedRows = expandSpace(space)
    expandedCols = expandSpace(space.T)
    galaxies = findGalaxies(space)
    print(f"Part 1: {int(getDistances(galaxies, expandedRows, expandedCols, 2))}")
    print(f"Part 2: {int(getDistances(galaxies, expandedRows, expandedCols, 1000000))}")
