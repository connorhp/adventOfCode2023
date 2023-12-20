def findComp(nums, num):
    for n in nums:
        if n[3] == num[3] and n[4] == num[4] and num[0] != n[0]:
            n[1] = False
            num[1] = False
            #print("multiplying: " + str(num[0]) + " and " + str(n[0]) + " which = " + str(n[0] * num[0]))
            return n[0] * num[0]
    return 0

def checkSurroundings(grid, i, j):
    if i != 0:
        if grid[i - 1][j] != '.':
            # print(grid[i - 1][j])
            return True, grid[i - 1][j], i-1,j
    if i != len(grid) - 1:
        if grid[i + 1][j] != '.':
            # print(grid[i + 1][j])
            return True, grid[i + 1][j], i+1, j
    if j != 0:
        if not str(grid[i][j - 1]).isnumeric() and grid[i][j - 1] != '.':
            # print(grid[i][j - 1])
            return True, grid[i][j - 1], i, j-1
    if j != len(grid[0]) - 1:
        if not str(grid[i][j + 1]).isnumeric() and grid[i][j + 1] != '.':
            # print(grid[i][j + 1])
            return True, grid[i][j + 1], i, j+1

    if i != 0 and j != 0:
        if grid[i - 1][j - 1] != '.':
            # print(grid[i - 1][j - 1])
            return True, grid[i - 1][j - 1], i-1, j-1
    if i != 0 and j != len(grid[0]) - 1:
        if grid[i - 1][j + 1] != '.':
            # print(grid[i - 1][j + 1])
            return True, grid[i - 1][j + 1], i-1, j+1
    if i != len(grid) - 1 and j != 0:
        if grid[i + 1][j - 1] != '.':
            # print(grid[i + 1][j - 1])
            return True, grid[i + 1][j - 1], i+1, j-1
    if i != len(grid) - 1 and j != len(grid[0]) - 1:
        if grid[i + 1][j + 1] != '.':
            # print(grid[i + 1][j + 1])
            return True, grid[i + 1][j + 1], i+1, j+1
    return False, '', -1, -1

if __name__ == '__main__':
    with open("day3.txt", "r") as f:
        grid = [[*line[:-1]] for line in f.readlines()]
        ans = 0
        nums = []
        for i, row in enumerate(grid):
            num = ""
            symbol = ""
            touches = False
            symi = -1
            symj = -1
            for j, col in enumerate(row):
                if str(col).isnumeric():
                    letterTouch, what, si, sj = checkSurroundings(grid, i, j)
                    if touches is not True:
                        touches = letterTouch
                        symbol = what
                        symi = si
                        symj = sj

                    num += col
                elif num != "":
                    nums.append([int(num), touches, symbol, symi, symj])
                    num = ""
                    symbol = ""
                    touches = False
                    symi = -1
                    symj = -1
            if num != "":
                nums.append([int(num), touches, symbol, symi, symj])

        print(nums)
        part1 = 0
        for num in nums:
            if num[1] is True:
                part1 += num[0]

        part2 = 0
        for num in nums:
            if num[1] is True:
                if num[2] == '*':
                    part2 += findComp(nums, num)
        print(f"Part 1: {part1}")
        print(f"Part 2: {part2}")

