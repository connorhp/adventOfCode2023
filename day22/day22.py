import copy


def parse():
    bricks = []
    for line in open("day22.txt", "r").readlines():
        brick = line.replace('\n', '').split('~')
        coords = [[int(y) for y in x.split(',')] for x in brick]
        bricks.append(coords)
    return bricks


def canCollapse(xy, xy1):
    for i in range(len(xy)):
        for j in range(len(xy[0])):
            if xy1[i][j] != '.' and xy[i][j] != '.':
                return False
    return True

def collapseIt(xy,xy1):
    newz = copy.deepcopy(xy)
    for i in range(len(xy)):
        for j in range(len(xy[0])):
            if xy1[i][j] != '.':
                newz[i][j] = xy1[i][j]
    return newz

def canDisintegrate(xy, xy1):
    supports = {}
    for i in range(len(xy)):
        for j in range(len(xy[0])):
            if xy1[i][j] != '.':
                if xy[i][j] != '.' and xy[i][j] != xy1[i][j]:
                    if xy1[i][j] in supports:
                        sup = supports[xy1[i][j]]
                        sup.update({xy[i][j]})
                    else:
                        supports.update({xy1[i][j]: {xy[i][j]}})
    return supports

def part1(bricks):
    bricks = sorted(bricks, key=lambda x:x[0][0])
    xlen = bricks[-1][0][0] - bricks[0][0][0]
    bricks = sorted(bricks, key=lambda x: x[0][1])
    ylen = bricks[-1][0][1] - bricks[0][0][1]
    bricks = sorted(bricks, key=lambda x: x[0][2])
    area = {}
    xyz = []
    for i, brick in enumerate(bricks):
        x1, y1, z1 = brick[0]
        x2, y2, z2 = brick[1]
        x = ['.' for _ in range(xlen+1)]
        grid = [['.' for x in range(xlen+1)] for y in range(ylen+1)]
        x[x1:x2+1] = str(i%9) * (x2+1-x1)
        grid[y1:y2+1] = [x] * (y2+1-y1)
        for _ in range(z2 - z1 + 1):
            xyz.append(grid)
    for xy in xyz:
        print(xy)
    print()
    newGrid = []
    beenCollapsed = False
    for i, xy in enumerate(xyz):
        if beenCollapsed:
            beenCollapsed = False
            continue
        if i == len(xyz) -1:
            newGrid.append(xy)
            break
        xy1 = xyz[i+1]
        collapsable = canCollapse(xy, xy1)
        if collapsable:
            changed = True
            beenCollapsed = True
            newGrid.append(collapseIt(xy,xy1))
        else:
            newGrid.append(xy)
    for xy in newGrid:
        print(xy)
    print()
    xyz = newGrid
    disintegrates = set()
    for i, xy in enumerate(xyz):
        if i == len(xyz) - 1:
            break
        xy1 = xyz[i + 1]
        supports = canDisintegrate(xy, xy1)
        cand = set()
        for support in supports.keys():
            sup = supports[support]
            if len(sup) > 1:
                cand.update(sup)
            if len(sup) == 1 and sup in cand:
                    cand.remove(sup)
            # if len(sup) == 0:
            #     cand.update(support)
        disintegrates.update(cand)
    print(disintegrates)




if __name__ == "__main__":
    data = parse()
    print(data)
    part1(data)


    # bricks = sorted(bricks, key=lambda x:x[0][0])
    # xlen = bricks[-1][0][0] - bricks[0][0][0]
    # bricks = sorted(bricks, key=lambda x: x[0][1])
    # ylen = bricks[-1][0][1] - bricks[0][0][1]
    # zlen = len(bricks)
    # print(xlen, ylen, zlen)
    # bricks = sorted(bricks, key=lambda x: x[0][2])
    # print(bricks)
    # xyz = [[['.'for k in range(zlen)] for j in range(ylen+1)] for i in range(xlen+1)]
    # print(xyz)
    # for i, brick in enumerate(bricks):
    #     x1,y1,z1 = brick[0]
    #     x2,y2,z2 = brick[1]
    #     if min(z1, z2) > i:
    #         fall()