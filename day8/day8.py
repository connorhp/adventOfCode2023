import math
import time


def parseData2():
    with open("day8.txt", "r") as f:
        code = f.readline()[:-1]
        path = {}
        pathList = []
        aPos = []
        i = 0
        for line in f.readlines():
            if line != '\n':
                line = line.replace('\n', '')
                mapp = line.split(" = ")
                where = mapp[0].strip()
                if where[-1] == 'A':
                    aPos.append(i)
                going = mapp[1].strip()[1:-1].split(", ")
                pathList.append([where, going])
                path.update({where: going})
                i += 1
        return code, path, pathList, aPos


def parseData1():
    with open("day8.txt", "r") as f:
        code = f.readline()[:-1]
        path = {}
        pathList = []
        aPos = -1
        i = 0
        for line in f.readlines():
            if line != '\n':
                line = line.replace('\n', '')
                mapp = line.split(" = ")
                where = mapp[0].strip()
                if where == "AAA":
                    aPos = i
                going = mapp[1].strip()[1:-1].split(", ")
                pathList.append([where, going])
                path.update({where: going})
                i += 1
        # print(path)
        return code, path, pathList, aPos


def part1(code, path, pathList, aPos):
    current, going = pathList[aPos]
    codePos = 0
    steps = 0
    while True:
        if current == "ZZZ":
            break
        steps += 1
        if code[codePos % len(code)] == 'L':
            current = going[0]
            going = path.get(going[0])
        elif code[codePos % len(code)] == 'R':
            current = going[1]
            going = path.get(going[1])
        codePos += 1
    return steps


def getLCM(nums):
    multiple = nums[0]
    for num in nums:
        multiple = lcm(multiple, num)
    return multiple


def gcd(a, b):
    while b != 0:
        a1 = b
        b = a % b
        a = a1
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def part2(code, path, pathList, aPos):
    tSteps = []
    for a in aPos:
        subStart = time.perf_counter()
        current, going = pathList[a]
        codePos = 0
        steps = 0
        while True:
            if current[-1] == "Z":
                break
            steps += 1
            if code[codePos % len(code)] == 'L':
                current = going[0]
                going = path.get(going[0])
            elif code[codePos % len(code)] == 'R':
                current = going[1]
                going = path.get(going[1])
            codePos += 1
        # print(f"{pathList[a][0]}: steps: {steps}")
        tSteps.append(steps)
    return math.lcm(*tSteps)


def part2Brute(code, path, pathList, aPos):
    currents = [pathList[a] for a in aPos]
    codePos = 0
    steps = 0
    while True:
        steps += 1
        for i, (current, going) in enumerate(currents):
            if code[codePos % len(code)] == 'L':
                currents[i][0] = going[0]
                currents[i][1] = path.get(going[0])
            elif code[codePos % len(code)] == 'R':
                currents[i][0] = going[1]
                currents[i][1] = path.get(going[1])
        allZ = True
        for current, going in currents:
            if current[-1] != 'Z':
                allZ = False
                break
        if allZ:
            break
        else:
            codePos += 1
    return steps


if __name__ == '__main__':
    #code, path, pathList, aPos = parseData1()
    #print(f"Part 1: {part1(code, path, pathList, aPos)}")
    #print(f"Part 2: {part2(code, path, pathList, aPos)}")
    print(f"Part 2: {part2Brute(*parseData2())}")
