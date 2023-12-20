def parse():
    with open("day9.txt", "r") as f:
        sequences = []
        for line in f.readlines():
            line = line.replace('\n', '')
            nums = line.split()
            sequences.append([int(x) for x in nums])
    return sequences


def rec(d):
    new = []
    for i in range(len(d) - 1):
        new.append(d[i + 1] - d[i])
    if new.count(0) == len(new):
        return new[-1] + d[-1]
    else:
        return rec(new) + d[-1]


def recursion(data):
    ans = 0
    for sequence in data:
        ans += rec(sequence)
    print(f"Part 1: {ans}")
    ans = 0
    for sequence in data:
        sequence = sequence[::-1]
        ans += rec(sequence)
    print(f"Part 2: {ans}")

if __name__ == '__main__':
    sequences = parse()
    recursion(sequences)
