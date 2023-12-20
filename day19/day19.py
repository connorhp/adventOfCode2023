from copy import deepcopy


def parse():
    workflows = {}
    ratings = []
    inWorkFlows = True
    for line in open("day19.txt", "r").readlines():
        if line == '\n':
            inWorkFlows = False
            continue
        line = line.replace('\n', '')
        line = line.replace('{', ' ')
        line = line.replace('}', ' ')
        line = line.replace(',', ' ').strip()
        if inWorkFlows:
            line = line.split(' ')
            name = line[0]
            cons = line[1:]
            workflows.update({name: cons})
        else:
            line = line.split(' ')
            temp = {}
            for l in line:
                let, num = l.split('=')
                temp.update({let: num})
            ratings.append(temp)
    return workflows, ratings

def mapit(flow, rate):
    for i, f in enumerate(flow):
        if i == len(flow) -1:
            return f
        let = f[0]
        con = f[1]
        colon = f.index(':')
        num = int(f[2:colon])
        truth = f[colon+1:]
        if con == '<':
            if int(rate[let]) < num:
                return truth
        if con == '>':
            if int(rate[let]) > num:
                return truth




def part1(flows, rates):
    verdicts = []
    for rate in rates:
        hasVerdict = False
        flow = flows["in"]
        while not hasVerdict:
            truth = mapit(flow, rate)
            if truth == 'A' or truth == 'R':
                hasVerdict = True
                verdicts.append((rate, truth))
            else:
                # print(f" {rate} going to flow {truth}")
                flow = flows[truth]
        # print()
    ans = 0
    for verdict in verdicts:
        # print(verdict)
        if verdict[1] == 'A':
            xmas = verdict[0]
            ans += int(xmas['x']) + int(xmas['m']) + int(xmas['a']) + int(xmas['s'])
    print(f"Part 1: {ans}")

accepted = []

def mult(xmas):
    ans = 1
    for let in "xmas":
        ans *= (xmas[let][1] - xmas[let][0]+1)
    return ans

def find(flows, xmas, flow, t):
    print(f"{t} {xmas}")
    for f in flow:
        if f == flow[-1]:
            if f == 'A':
                print(f"{f} -> {xmas} -> {mult(xmas)}")
                accepted.append(mult(xmas))
                continue
            elif f == 'R':
                print(f"{f} -> {xmas}")
                continue
            find(flows, xmas, flows[f], f)
        else:
            let = f[0]
            con = f[1]
            colon = f.index(':')
            num = int(f[2:colon])
            truth = f[colon+1:]
            if con == '<':
                num -= 1
                xmasT = deepcopy(xmas)
                xmasT[let][1] = num
                if truth == 'A':
                    print(f"{f} -> {xmasT} ->{mult(xmasT)}")
                    accepted.append(mult(xmasT))
                    xmas[let][0] = num+1
                    continue
                elif truth == 'R':
                    print(f"{f} -> {xmasT}")
                    xmas[let][0] = num+1
                    continue
                find(flows, xmasT, flows[truth], truth)
                xmas[let][0] =num+1
            elif con == '>':
                num += 1
                xmasT = deepcopy(xmas)
                xmasT[let][0] =num
                if truth == 'A':
                    print(f"{f} -> {xmasT} ->{mult(xmasT)}")
                    accepted.append(mult(xmasT))
                    xmas[let][1] = num-1
                    continue
                elif truth == 'R':
                    print(f"{f} -> {xmasT}")
                    xmas[let][1] = num-1
                    continue
                find(flows, xmasT, flows[truth], truth)
                xmas[let][1] = num-1

def part2(flows):
    sets = {'x': [1,4000], 'm': [1,4000], 'a':[1,4000], 's':[1,4000]}
    flow = flows["in"]
    find(flows, sets, flow, "in")
    print(4000**4)
    print(167_409_079_868_000)
    print(accepted)
    print(sum(accepted))


if __name__ == "__main__":
    workflows, ratings = parse()
    print(workflows["in"])
    # print(ratings[0])
    #print((400 ** 4) * 5)
    part1(workflows, ratings)
    part2(workflows)