import numpy as np


def prettyPrint(grid):
    for row in grid:
        for char in row:
            print(char, end='')
        print()
    print()



def parse():
    grid = []
    with open("day14.txt", "r") as f:
        for line in f.readlines():
            line = line.replace('\n', '')
            grid.append(list(line))
    return np.asarray(grid)

def tilt(mirrors):
    tilted = []
    for row in mirrors:
        sects = ''.join(x for x in row).split('#')
        tempRow = ""
        for sect in sects:
            numMirror = sect.count('O')
            numDots = sect.count('.')
            tempRow += 'O'*numMirror + '.'*numDots + '#'

        tilted.append(list(tempRow[:-1]))
    return np.asarray(tilted)

def count(tilted):
    gridAns = 0
    leng = len(tilted)
    for i, row in enumerate(tilted):
        gridAns += (len(tilted) - i) * row.tolist().count('O')
    return gridAns


def part1(mirrors):
    tilted = tilt(mirrors.T).T
    #prettyPrint(tilted)
    ans = count(tilted)
    print(f"Part 1: {ans}")

def fullRotate(mirror):
    mirror = tilt(mirror.T).T  # North
    mirror = tilt(mirror)  # West
    mirror = np.flip(tilt(np.flip(mirror).T)).T  # South
    mirror = np.flip(tilt(np.flip(mirror)))  # East
    #print(mirror)
    return mirror

def findCycles(mirrors):
    cycles = []
    for i in range(100000000):
        mirrors =fullRotate(mirrors)
        for j,cycle in enumerate(cycles):
            if np.equal(cycle, mirrors).all():
                print(f"EQUAL: {j} {len(cycles)}")
                #break
                return cycles[j:], j
                # prettyPrint(mirrors)
                # prettyPrint(cycle)

        cycles.append(mirrors)


def part2(mirrors):
    cycles, start = findCycles(mirrors)
    billionRem = (1_000_000_000-start) % len(cycles)
    print(f"start: {start} cycleLen: {len(cycles)} billionRem: {billionRem}")
    print(f"Part 2: {count(cycles[billionRem-1])}")


if __name__ == '__main__':
    grid = parse()
    part1(grid)
    part2(grid)