def parse():
    codes = []
    for line in open("day15.txt","r").readlines():
        codes.extend(line.replace('\n', '').split(','))
    return codes

def prettyPrint(boxes):
    for i, box in enumerate(boxes):
        if len(box) != 0:
            print(f"Box {i}: {box}")
    print()


def hashify(code):
    codeAns = 0
    for let in code:
        codeAns += ord(let)
        codeAns *= 17
        codeAns %= 256
    return codeAns

def part1(codes):
    ans = 0
    for code in codes:
        codeAns = hashify(code)
        #print(f"{code} -> {codeAns}")
        ans += codeAns
    print(f"Part 1: {ans}")

def boxeql(box, asc, c):
    for i, (lens, label) in enumerate(box):
        if lens == asc:
            box[i] = [asc, c]
            return box
    box.append([asc, c])
    return box

def boxMin(box, asc):
    newBox = []
    for lens, label in box:
        if lens != asc:
            newBox.append([lens, label])
    return newBox

def getAnsPart2(boxes):
    ans = 0
    for i, box in enumerate(boxes):
        if len(box) != 0:
            for j, (lens, label) in enumerate(box):
                tempAns = (i+1) * (j+1) * int(label)
                ans += tempAns
                #print(f"{lens}: {label} = {tempAns}")
    return ans


def part2(codes):
    boxes = [[] for x in range(256)]
    for code in codes:
        if code.count('=') == 1:
            asc, c = code.split('=')
            ascAns = hashify(asc)
            boxes[ascAns] = boxeql(boxes[ascAns], asc, c)
        elif code.count('-') == 1:
            asc = code[:-1]
            ascAns = hashify(asc)
            boxes[ascAns] = boxMin(boxes[ascAns], asc)
        #prettyPrint(boxes)
    print(f"Part 2: {getAnsPart2(boxes)}")




if __name__ == '__main__':
    codes = parse()
    part1(codes)
    part2(codes)