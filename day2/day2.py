import re


def part1():
    with open("day2.txt", "r") as f:
        part1 = 0
        for line in f.readlines():
            line = line[:-1]
            colon = line.find(":")
            game = re.sub(r'[A-Za-z]', "", line[:colon])
            gameWorks = True
            for marbles in line[colon + 1:].split(";"):
                r = 12
                g = 13
                b = 14
                for marble in marbles.split(','):
                    color = marble.replace(" ", "")
                    amount = re.sub(r'[A-Za-z]', "", marble)
                    if "red" in color:
                        r -= int(amount)
                    if "green" in color:
                        g -= int(amount)
                    if "blue" in color:
                        b -= int(amount)
                if r < 0 or g < 0 or b < 0:
                    gameWorks = False
            if gameWorks:
                part1 += int(game)
        print(f"Part 1: {part1}")

def part2():
    with open("day2.txt", "r") as f:
        part2 = 0
        for line in f.readlines():
            line = line[:-1]
            colon = line.find(":")
            r = 0
            g = 0
            b = 0
            for marbles in line[colon + 1:].split(";"):
                for marble in marbles.split(','):
                    color = marble.replace(" ", "")
                    amount = re.sub(r'[A-Za-z]', "", marble.replace(" ", ""))
                    if "red" in color:
                        if int(amount) > r:
                            r = int(amount)
                    if "green" in color:
                        if int(amount) > g:
                            g = int(amount)
                    if "blue" in color:
                        if int(amount) > b:
                            b = int(amount)
            part2 += (r * g * b)
        print(f"Part 2: {part2}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part1()
    part2()
