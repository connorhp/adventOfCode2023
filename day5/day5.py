import math

import numpy as np
import time

sts = []
stf = []
ftw = []
wtl = []
ltt = []
tth = []
htl = []


def parseTable(f):
    if len(sts) != 0:
        return
    while True:
        line = f.readline()
        if not line:
            break
        if line[:-1] == "seed-to-soil map:":
            parseGroup(f, sts)
            # print(sts)
        if line[:-1] == "soil-to-fertilizer map:":
            parseGroup(f, stf)
            # print(stf)
        if line[:-1] == "fertilizer-to-water map:":
            parseGroup(f, ftw)
            # print(ftw)
        if line[:-1] == "water-to-light map:":
            parseGroup(f, wtl)
            # print(wtl)
        if line[:-1] == "light-to-temperature map:":
            parseGroup(f, ltt)
            # print(ltt)
        if line[:-1] == "temperature-to-humidity map:":
            parseGroup(f, tth)
            # print(tth)
        if line[:-1] == "humidity-to-location map:":
            parseGroup(f, htl)
            # print(htl)


def parseGroup(f, seedMap):
    while True:
        line = f.readline()
        if line == '\n' or not line:
            break
        if line[-1] == '\n':
            line = line[:-1]
        rangeMap = [int(x) for x in line.split(" ")]
        seedMap.append(rangeMap)


def convert(source, mapping):
    for d, s, r in mapping:
        if s <= source <= s + r:
            return d + source - s
    return source


def backConvert(dest, mapping):
    for d, s, r in mapping:
        if d <= dest < d + r:
            return s + dest - d
    return dest


def findLowest(seeds):
    # print(seeds)
    lowest = None
    for seed in seeds:
        location = findLoc(seed)
        if lowest is None or location < lowest:
            lowest = location
    return (lowest)


def findLoc(seed):
    # print(seeds)
    soil = convert(seed, sts)
    fert = convert(soil, stf)
    water = convert(fert, ftw)
    light = convert(water, wtl)
    temp = convert(light, ltt)
    humidity = convert(temp, tth)
    return convert(humidity, htl)


def findSeed(loc):
    humidity = backConvert(loc, htl)
    temp = backConvert(humidity, tth)
    light = backConvert(temp, ltt)
    water = backConvert(light, wtl)
    fert = backConvert(water, ftw)
    soil = backConvert(fert, stf)
    seed = backConvert(soil, sts)
    # print(f"loc {loc} -> hum {humidity} -> temp {temp} -> light {light} -> water {water} -> fert {fert} -> soil {soil} -> seed {seed}")
    return seed


def part1(seeds):
    print(f"Part 1: {findLowest(seeds)}")


def part2(seeds):
    loc = 0
    seeds = np.reshape(seeds, (int(len(seeds) / 2), 2))
    while True:
        seed = findSeed(loc)
        for start, seedRange in seeds:
            if start <= seed < (start + seedRange):
                # print(f"Found seed {seed} With Location {loc} in range {start} -> {start + seedRange - 1}")
                print(f"Part 2: {loc}")
                return
        loc += 1


def numpyAttempt(seeds):
    seeds = np.reshape(seeds, (int(len(seeds) / 2), 2))
    # print(seeds)
    lowest = None
    for start, seedRange in seeds:
        subStart = time.perf_counter()
        seeds = np.arange(start, start + seedRange)
        mapping = np.vectorize(findLoc)
        loc = np.min(mapping(seeds))
        subEnd = time.perf_counter()
        print(f"loc = {loc} Time took in {subEnd - subStart:0.2f} seconds")
    print(lowest)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open("day5.txt", "r") as f:
        seeds = [int(x) for x in f.readline()[7:].split(" ")]
        parseTable(f)
        part1(seeds)
        subStart = time.perf_counter()
        part2(seeds)
        subEnd = time.perf_counter()
        print(f"Found Part 2 in {subEnd - subStart:0.2f} seconds")
