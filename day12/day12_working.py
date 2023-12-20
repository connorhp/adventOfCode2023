import time
from functools import cache
from math import log2

from tqdm import tqdm


def parse():
    springs = []
    with open("day12.txt", "r") as f:
        for line in f.readlines():
            line = line.replace('\n', '')
            springs.append(line.split(" "))
    return springs

def works(springLine, amo):
    amos = amo.split(',')
    springs = springLine.replace('.', ' ').split()
    if len(springs) == len(amos):
        for i in range(len(springs)):
            if len(springs[i]) != int(amos[i]):
                return 0
        return 1
    return 0

@cache
def getPossabilities(springLine, amo):
    if len(springLine) == 0:
        if len(amo) == 0:
            return 1
        else:
            return 0
    elif len(amo) == 0:
        if springLine.count('#') > 0:
            return 0
        else:
            return 1
    elif springLine[0] == '.':
        return getPossabilities(springLine[1:], amo)
    elif springLine[0] == '#':
        amo = [int(x) for x in amo.split(',')]
        temp = '.'.join(springLine.split('.')).split('.')
        if len(temp[0]) == amo[0]:
            springLine=springLine[amo[0]:]
            amo = amo[1:]
            strAmo = ','.join([str(x) for x in amo])
            return getPossabilities(springLine, strAmo)
        elif len(temp[0]) > amo[0]:
            temp = temp[0].split('?')
            if len(temp[0]) > amo[0]:
                return 0
            elif len(temp[0]) < amo[0]:
                amo[0] -= 1
                springLine=springLine[1:]
                strAmo = ','.join([str(x) for x in amo])
                return getPossabilities(springLine.replace('?', '#', 1), strAmo)
            else:
                springLine = springLine[amo[0]:]
                if len(springLine) > 0:
                    springLine = springLine[1:]
                amo = amo[1:]
                strAmo = ','.join([str(x) for x in amo])
                return getPossabilities(springLine, strAmo)
        else:
            return 0
    elif springLine[0] == '?':
        return getPossabilities(springLine.replace('?', '#', 1), amo) + getPossabilities(springLine.replace('?', '.', 1), amo)

def part1(springs):
    ans = 0
    start = time.perf_counter()
    for springLine, amo in springs:
        # print(springLine)
        ans += getPossabilities(springLine, amo)
    print(f"Part 1: {ans} in {time.perf_counter() - start:.2f} seconds")

def part2(springs):
    totalPos = 0
    ans = 0
    start = time.perf_counter()
    for springLine, amo in springs:
        lineTotalPos = 0
        og = getPossabilities(springLine, amo)
        bef = 2 ** (log2(og) + 4 * log2(getPossabilities('?' + springLine, amo)))
        aft = 2 ** (log2(og) + 4 * log2(getPossabilities(springLine + '?', amo)))
        quinSping, quinAmo = quintuple(springLine, amo)
        quin = getPossabilities(quinSping, quinAmo)
        lineTotalPos += quinSping.count('?')
        if quin == bef and quin == aft:
            matches = "BOTH"
        elif quin == bef:
            matches = "BEFORE"
        elif quin == aft:
            matches = "AFTER"
        else:
            matches = "NEITHER"

        print(f"{springLine.ljust(20)} {amo.ljust(15)} PART1 {str(og).ljust(5)}"
              f" BEF {str(round(bef)).ljust(12)} AFT  {str(round(aft)).ljust(12)}"
              f" PART2 {str(quin).ljust(12)} MATCHES: {matches.ljust(8)} POS  2^{lineTotalPos}")
        ans += quin
        totalPos += lineTotalPos
    print(f"Part 2: {ans} Total Possabilities: 2^{totalPos} in {time.perf_counter() - start:.2f} seconds")

def quintuple(springLine, amo):
    springLine = '?'.join([springLine] * 5)
    amo = ','.join([amo] * 5)
    return springLine, amo


if __name__ == '__main__':
    springs = parse()
    part1(springs)
    part2(springs)