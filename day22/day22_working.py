import copy

from tqdm import tqdm


def parse():
    bricks = []
    for line in open("day22.txt", "r").readlines():
        brick = line.replace('\n', '').split('~')
        coords = [[int(y) for y in x.split(',')] for x in brick]
        bricks.append(coords)
    return bricks

def intersects(b,s):
    return len(set(b).intersection(s)) > 0

def fall(brick, settled):
    x, y, z = brick[0]
    x1, y1, z1 = brick[1]
    if x == 4 and y == 7:
        pass
    if z == 1:
       return brick
    bx = range(x, x1+1)
    by = range(y, y1+1)
    for settle in reversed(settled):
        sx, sy, sz = settle[0]
        sx1, sy1, sz1 = settle[1]
        sx = range(sx, sx1 + 1)
        sy = range(sy, sy1 + 1)
        if intersects(bx, sx) and intersects(by, sy):
            drop = abs(z - sz1) - 1
            return [[x,y, z-drop],[x1,y1,z1-drop]]
    drop = z-1
    return [[x,y, z-drop],[x1,y1,z1-drop]]


def collapse(data):
    bricks = sorted(data, key=lambda x: x[0][2])
    settled = []
    numFallen = 0
    for brick in bricks:
        z = brick[0][2]
        if z > 1:
            newBrick = fall(brick, settled)
            if newBrick != brick:
                numFallen += 1
                brick = newBrick
        settled.append(brick)
        settled = sorted(settled, key=lambda x: x[1][2])
    return settled, numFallen

def part1(data):
    settled, _ = collapse(data)
    print(settled)
    falls = []
    for settle in tqdm(settled):
        cop = copy.deepcopy(settled)
        cop.remove(settle)
        _, fallen = collapse(cop)
        falls.append(fallen)
    print(falls)
    print(falls.count(0))
    print(sum(falls))

if __name__ == "__main__":
    data = parse()
    part1(data)