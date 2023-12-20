rankingJoker = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
rankingNotJoker = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
ranking = []


def isHigher(hand1, hand2):
    for card1, card2 in zip(hand1, hand2):
        if ranking.index(card1) > ranking.index(card2):
            return True
        if ranking.index(card2) > ranking.index(card1):
            return False


def getStrength(hand, joker):
    numJoker = 0
    has5 = False
    has4 = False
    has3 = False
    num2 = 0
    for card in hand:
        if card == 'J' and joker:
            numJoker += 1
            continue
        if hand.count(card) == 5:
            has5 = True
        if hand.count(card) == 4:
            has4 = True
        if hand.count(card) == 3:
            has3 = True
        if hand.count(card) == 2:
            num2 += 0.5

    if has5 or (numJoker == 1 and has4) or (numJoker == 2 and has3) or (
            numJoker == 3 and int(num2) == 1) or numJoker == 4 or numJoker == 5:
        return 6
    elif has4 or (numJoker == 1 and has3) or (numJoker == 2 and int(num2) == 1) or (numJoker == 3 and int(num2) == 0):
        return 5
    elif (has3 and int(num2) == 1) or (numJoker == 1 and int(num2) == 2):
        return 4
    elif has3 or (numJoker == 1 and num2 == 1) or (numJoker == 2 and int(num2) == 0):
        return 3
    elif int(num2) == 2:
        return 2
    elif int(num2) == 1 or (numJoker == 1 and int(num2) == 0):
        return 1
    return 0


def parseData(f, joker):
    data = []
    for line in f.readlines():
        line = line.replace('\n', '').split(" ")
        data.append([line[0], int(line[1]), 1, getStrength(line[0], joker)])
    return data


def isStronger(hand1, hand2):
    if hand1 == hand2:
        return False
    return isHigher(hand1, hand2)


def sort(data):
    winnings = 0
    for i, (hand, bet, rank, strength) in enumerate(data):
        for h, b, r, s in data:
            if hand == h:
                continue
            elif strength > s or (strength == s and isStronger(hand, h)):
                data[i][2] += 1
    for h, b, r, s in data:
        winnings += r * b
    return winnings


def getAns(f, part):
    global ranking
    if part == 1:
        ranking = rankingNotJoker
    if part == 2:
        ranking = rankingJoker
    data = parseData(f, part != 1)
    print(f"Answer for part {part} is {sort(data)}")


if __name__ == '__main__':
    with open("day7.txt", "r") as f:
        getAns(f, 1)
        f.seek(0)
        getAns(f, 2)
