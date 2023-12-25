from z3.z3 import *

if __name__ == "__main__":
    def parse():
        hails = []
        for line in open("day24.txt", "r").readlines():
            hail = line.replace('\n', '').split('@')
            coords = [[int(y) for y in x.split(',')] for x in hail]
            hails.append(coords)
        return hails
    data = parse()
    # s = 200000000000000
    # e = 400000000000000
    s = 200000000000000
    e = 400000000000000
    # def getPos(st, px, pxv, py, pyv):
    #     pxs = (st-px) / pxv
    #     pys = (st-py) / pyv
    #     return st if ps >= 0 else p

    def inFuture(x, vx, y, vy, ix, iy):
        tx = (ix - x) / vx
        ty = (iy - y) / vy
        return tx >= 0 and ty >= 0

    def part1(hailstones):
        intersections = 0
        for i in range(len(hailstones)-1):
            hailA = hailstones[i]
            ax, ay, _ = hailA[0]
            avx, avy, _ = hailA[1]
            ax1 = ax +avx
            ay1 = ay + avy
            ma = (ay1-ay) / (ax1 -ax)
            ba = ay - (ax * ma)
            for j in range(i+1, len(hailstones)):
                hailB = hailstones[j]
                bx, by, _ = hailB[0]
                bvx, bvy, _ = hailB[1]
                bx1 = bx + bvx
                by1 = by + bvy
                mb = (by1 - by) / (bx1 - bx)
                bb = by - (bx * mb)
                try:
                    xinter = (ba - bb) / (mb - ma)
                    yinter = xinter* mb + bb
                    if s < xinter < e and s < yinter < e:
                        if inFuture(ax, avx, ay, avy, xinter, yinter) and inFuture(bx, bvx, by, bvy, xinter, yinter):
                            #print(f"{hailstones[i]} and {hailstones[j]} intersect at {xinter}, {yinter}")
                            intersections +=1
                except:
                    pass
        print(f"Part 1: {intersections}")


    def part2(hailstones):
        x = Real('x')
        y = Real('y')
        z = Real('z')
        vx = Real('vx')
        vy = Real('vy')
        vz = Real('vz')
        solver = Solver()
        for i in range(len(hailstones)):
            hailA = hailstones[i]
            ax, ay, az = hailA[0]
            avx, avy, avz = hailA[1]
            t = Real(f't_{i}')
            solver.add(t >= 0)
            solver.add(x + vx*t == ax + avx * t)
            solver.add(y + vy * t == ay + avy * t)
            solver.add(z + vz * t == az + avz * t)
        assert solver.check() == sat
        model = solver.model()
        x = model.eval(x)
        y = model.eval(y)
        z = model.eval(z)
        x = x.as_long()
        y = y.as_long()
        z = z.as_long()
        print(x, y, z)
        print(f"Part 2 {x + y + z}")

    #part1(data)
    part2(data)