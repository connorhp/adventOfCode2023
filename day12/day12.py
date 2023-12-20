import math
import time
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
                return False
        return True
    return False

def getPossabilitiesAndChanged(springLine, amo):
    numQues = springLine.count('?')
    tempAns = 0
    working = []
    # changes = [False for x in range(len(springLine))]
    for i in range(2 ** numQues):
        tempString = springLine
        for c in str(bin(i)[2:]).zfill(numQues):
            if c == '0':
                tempString = tempString.replace('?', '.', 1)
            elif c == '1':
                tempString = tempString.replace('?', '#', 1)
        if works(tempString, amo):
            working.append(tempString)
            # for j in range(len(changes)):
            #     if working[j] != tempString[j]:
            #         changes[j] = True
            # print(f"{springLine} -> {tempString} = {amo}")
            tempAns += 1
    #print(tempAns)
    return tempAns, working

def getPossabilities(springLine, amo):
    numQues = springLine.count('?')
    tempAns = 0
    for i in (range(2 ** numQues)):
        tempString = springLine
        for c in str(bin(i)[2:]).zfill(numQues):
            if c == '0':
                tempString = tempString.replace('?', '.', 1)
            elif c == '1':
                tempString = tempString.replace('?', '#', 1)
        if works(tempString, amo):
            print(f"{springLine} -> {tempString} = {amo}")
            tempAns += 1
    #print(tempAns)
    return tempAns

def part1(springs):
    ans = 0
    start = time.perf_counter()
    #with tqdm(springs) as progress:
    for springLine, amo in springs:
        # print(springLine)
        # springLine, amo = quintuple(springLine, amo)
        ans += getPossabilities(springLine, amo)
    print(f"Part 1: {ans} in {time.perf_counter() - start:.2f} seconds")


def getUse(springLine, amo, working, tempAns):
    _, quinAmo = quintuple(springLine, amo)
    mult = 4
    springBef = '?' + springLine
    springAft = springLine + '?'
    tempBef, workingBef = getPossabilitiesAndChanged(springBef, amo)
    tempBef = mult * math.log2(tempBef) + tempAns
    tempAft, workingAft = getPossabilitiesAndChanged(springAft, amo)
    tempAft = mult * math.log2(tempAft) + tempAns
    use = springLine
    if len(workingBef) > len(workingAft):
        BefWorks = True
        for workbef in workingBef:
            for work in working:
                fullbef = work + (workbef * 4)
                #print(fullbef)
                if not works(fullbef, quinAmo):
                    BefWorks = False
                    break
            if not BefWorks:
                break
        if BefWorks:
            #print("Returning bef")
            return springBef
        else:
            #print("Returning aft")
            return springAft
    else:
        aftWorks = True
        for workAft in workingAft:
            for work in working:
                fullAft = (workAft * 4) + work
                #print(fullbef)
                if not works(fullAft, quinAmo):
                    aftWorks = False
                    break
            if not aftWorks:
                break
        if aftWorks:
            #print("Returning aft")
            return springAft
        else:
            #print("Returning bef")
            return springBef
    # print(changed + changedBef, changedAft + changed)

def part2(springs):
    ans = 0
    start = time.perf_counter()
    with tqdm(springs) as progress:
        for springLine, amo in progress:
            # print(springLine)
            temp, changed = getPossabilitiesAndChanged(springLine, amo)
            tempAns = math.log2(temp)
            #print(changed, amo)
            _, quinAmo = quintuple(springLine, amo)
            mult = 4
            use = getUse(springLine, amo, changed, tempAns)
            tempAns += mult * math.log2(getPossabilities(use, amo))
            ans += round(2**tempAns)
                # print(springLine, amo, "->", round(2 ** tempAns))
    print(f"Part 2: {ans} in {time.perf_counter() - start:.2f} seconds")

def quintuple(springLine, amo):
    springLine += '?' + springLine + '?' + springLine + '?' + springLine + '?' + springLine
    amo += ',' + amo + ',' + amo + ',' + amo + ',' + amo
    return springLine, amo


if __name__ == '__main__':
    springs = parse()
    part1(springs)
    #part2(springs)