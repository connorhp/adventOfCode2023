import math
import re
import time

import numpy as np


def parseData1(f):
    d = []
    for line in f.readlines():
        line = line[line.index(':') + 1:].strip().replace('\n', '')
        line = re.sub(' +', ' ', line)
        row = [int(x) for x in line.split(' ')]
        d.append(row)
    ndata = np.asarray(d)
    return np.rot90(np.fliplr(ndata))


def parseData2(f):
    d = []
    for line in f.readlines():
        line = line[line.index(':') + 1:].strip().replace('\n', '')
        line = re.sub(' +', '', line)
        d.append(int(line))
    return [d]


def quadForm(a, b, c):
    # print(a, b, c)
    plus = (-1 * b + (math.sqrt(b * b - 4 * a * c))) / (2 * a)
    minus = (-1 * b - (math.sqrt(b * b - 4 * a * c))) / (2 * a)
    # print(plus, minus)
    return [plus, minus]


def getAns(data):
    ans = 1
    for time, dist in data:
        quad = quadForm(1, -time, dist)
        mini = min(quad)
        maxi = max(quad)
        r = len(range(math.ceil(mini + .01), math.floor(maxi - .01) + 1))
        ans *= r
    return ans


if __name__ == '__main__':
    with open("day6.txt", "r") as f:
        data = parseData1(f)
        print(f"Part 1: {getAns(data)}")
        f.seek(0)
        data = parseData2(f)
        print(f"Part 2: {getAns(data)}")
