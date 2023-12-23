import copy

from shapely import LineString, Point
from tqdm import trange, tqdm
import shapely


def parse():
    bricks = []
    for line in open("day22.txt", "r").readlines():
        brick = line.replace('\n', '').split('~')
        coords = [[int(y) for y in x.split(',')] for x in brick]
        bricks.append(coords)
    return bricks

def intersects(s0,s1):
    return LineString(s0).intersects(LineString(s1))
    # dx0 = s0[1][0]-s0[0][0]
    # dx1 = s1[1][0]-s1[0][0]
    # dy0 = s0[1][1]-s0[0][1]
    # dy1 = s1[1][1]-s1[0][1]
    # p0 = dy1*(s1[1][0]-s0[0][0]) - dx1*(s1[1][1]-s0[0][1])
    # p1 = dy1*(s1[1][0]-s0[1][0]) - dx1*(s1[1][1]-s0[1][1])
    # p2 = dy0*(s0[1][0]-s1[0][0]) - dx0*(s0[1][1]-s1[0][1])
    # p3 = dy0*(s0[1][0]-s1[1][0]) - dx0*(s0[1][1]-s1[1][1])
    # return (p0*p1<=0) & (p2*p3<=0)

def distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**.5

def drop(brick, settled):
    x, y, z = brick[0]
    x1, y1, z1 = brick[1]
    if x == 1 and y == 8:
        pass
    isSettled = False
    for settle in reversed(settled):
        sx, sy, sz = settle[0]
        sx1, sy1, sz1 = settle[1]
        if sx -sx1 == sy-sy1 == 0 and x-x1 == y-y1 == 0:
            inter = x == sx and y == sy
        elif (sx-sx1 != 0 or sy-sy1 != 0) and x-x1 == y-y1 == 0:
            inter = distance((sx,sy), (x,y)) + distance((x,y), (sx1,sy1)) == distance((sx,sy), (sx1,sy1))
        elif sx -sx1 == sy-sy1 == 0 and (x-x1 != 0 or y-y1 != 0):
            inter = distance((sx,sy), (x,y)) + distance((x,y), (sx1,sy1)) == distance((sx,sy), (sx1,sy1))
        else:
            inter = intersects([[x,y],[x1,y1]], [[sx,sy],[sx1,sy1]])
        if  inter and max(sz1, sz) == min(z, z1)-1:
            return brick, True
    return [[x,y,z-1],[x1,y1,z1-1]], isSettled

def collapse(bricks):
    settled = []
    numFallen = 0
    for i, brick in enumerate(tqdm(bricks)):
        z = brick[0][2]
        isSettled = False
        fell = 0
        while z > 1 and not isSettled:
            brick, isSettled = drop(brick, settled)
            if not isSettled:
                fell = 1
            z = brick[0][2]
        numFallen += fell
        settled.append(brick)
        return settled, numFallen


def part1(bricks):
    bricks = sorted(bricks, key=lambda x: x[0][2])
    settled, _ = collapse(bricks)
    print(settled)
    print()

    supports = []
    for i, brick in enumerate(tqdm(settled)):
        copySettled = copy.deepcopy(settled)
        copySettled.remove(brick)
        _, timesFallen = collapse(copySettled)
        supports.append(timesFallen)
    print(supports)
    print(supports.count(0))

if __name__ == "__main__":
    data = parse()
    i = [[2,5],[10,10]]
    ii = [[9,9],[11,11]]
    line1 = LineString(i)
    line2 = LineString(ii)

    int_pt = line1.intersects(line2)
    part1(data)