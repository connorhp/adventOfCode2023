import re


def day1():
    with open("day1.txt", "r") as f:
        lines = f.readlines()
        part1 = 0
        for line in lines:
            line = re.sub(r'[A-Za-z]', "", line[:-1])
            num = "" + line[0] + "" + line[-1]
            part1 += int(num)
        print(f"Part 1: {part1}")

        part2 = 0
        for line in lines:
            print(line[:-1], end="")
            line = line.lower()[:-1]
            line = line.replace("oneight", "18")
            line = line.replace("twone", "21")
            line = line.replace("threeight", "38")
            line = line.replace("fiveight", "58")
            line = line.replace("sevenine", "79")
            line = line.replace("eightwo", "82")
            line = line.replace("eighthree", "83")
            line = line.replace("nineight", "98")

            line = line.replace("one", "1")
            line = line.replace("two", "2")
            line = line.replace("three", "3")
            line = line.replace("four", "4")
            line = line.replace("five", "5")
            line = line.replace("six", "6")
            line = line.replace("seven", "7")
            line = line.replace("eight", "8")
            line = line.replace("nine", "9")
            print(" -> " + line, end="")
            line = re.sub(r'[A-Za-z]', "", line)
            num = "" + line[0] + "" + line[-1]
            print(" -> " + num)

            part2 += int(num)
        print(f"Part 2: {part2}")


if __name__ == '__main__':
    day1()
