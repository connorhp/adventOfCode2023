# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re


def day2():
    with open("day2/day2.txt", "r") as f:
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
        print(part1)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
