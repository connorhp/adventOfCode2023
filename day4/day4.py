def getNumMatches(line):
    matches = 0
    line = line[:-1]
    colon = line.find(":")
    split = line.find("|")
    winning = line[colon + 1:split].split(" ")
    yours = line[split + 1:]
    # print("Card " + line[5])
    for num in yours.split(" "):
        try:
            winning.index(num)
            if num != '':
                # print("found: " + num)
                matches += 1
        except ValueError:
            pass
    return matches


def part1():
    with open("day4.txt", "r") as f:
        points = 0
        for line in f.readlines():
            numMatches = getNumMatches(line)
            if numMatches != 0:
                points += pow(2, int(numMatches) - 1)
        print(f"Part 1: {points}")


def part2():
    with open("day4.txt", "r") as f:
        scratchCards = 0
        # [[numCards, matches],...]
        cards = []
        for line in f.readlines():
            cards.append([1, getNumMatches(line)])
        print(cards)
        for i, card in enumerate(cards):
            for numCards in range(card[0]):
                for j, numMatches in enumerate(range(card[1])):
                    if i + j + 1 < len(cards):
                        cards[i + j + 1][0] += 1
        print(cards)
        total = 0
        for card in cards:
            total += card[0]
        print(f"Part 2: {total}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part1()
    part2()
