import math

from tqdm import trange


def parse():
    outputs = {}
    for line in open("day20.txt", "r").readlines():
        line = line.replace('\n', '')
        inout = line.split(" -> ")
        ins = inout[0]
        flip = ins[0] == '%'
        inv = ins[0] == '&'
        if flip or inv:
            ins = ins[1:]
        outs = inout[1]
        outputs.update({ins: (outs.split(', '), flip, inv)})
    return outputs


def sendSignal(outputs, part):
    # [current, beam, receivedFrom]
    queue = []
    # {tower: onoff}
    towers = {}
    numHigh = 0
    numLow = 0
    invs = {}
    rx = {}
    rang = 1000 if part == 1 else 1_000_000
    for tower in outputs.keys():
        towers.update({tower: False})
        casts, flip, inv = outputs[tower]
        for cast in casts:
            if cast in outputs:
                c, f, i = outputs[cast]
                if i:
                    if cast in invs:
                        watchers = invs[cast]
                        watchers.update({tower: "-"})
                        invs.update({cast: watchers})
                    else:
                        invs.update({cast: {tower:"-"}})
    for i in range(rang):
        queue.append(["broadcaster", '-', "button"])
        numLow += 1
        #print("button - to broadcaster")
        j = 0
        while queue:
            j += 1
            signal = queue[0]
            queue = queue[1:]
            tower, beam, recFrom = signal
            onoff = towers[tower]
            casts, flip, inv = outputs[tower]
            if tower == "nr" and beam == '+':
                pass
                #print("invs[nr]", invs["nr"])
                # print(invs["lh"], invs["fk"], invs["ff"], invs["mm"])
            sentData = True
            for cast in casts:
                sendBeam = beam
                if flip:
                    if beam == '+':
                        sentData = False
                        continue
                    elif beam == '-':
                        sendBeam = '-' if onoff else '+'

                if inv:
                    watchers = invs[tower]
                    watchers.update({recFrom: beam})
                    allHigh = True
                    for watch in watchers.keys():
                        if watchers[watch] == '-':
                            allHigh = False
                            break
                    sendBeam = '-' if allHigh else '+'
                if sendBeam == '-':
                    numLow += 1
                elif sendBeam == '+':
                    numHigh +=1
                #print(f"{tower} {sendBeam} -> {cast}")

                if cast in outputs:
                    queue.append([cast, sendBeam, tower])
            if flip and sentData:
                #print(f"Turning {tower} -> {not onoff}")
                onoff = not onoff
                towers.update({tower: onoff})
            for key in invs["nr"].keys():
                if key not in rx and invs["nr"][key] == '+':
                    #print(invs["nr"])
                    #print(f"watcher {key} changed to + after button press {i+1}")
                    rx.update({key : i+1})
        if len(rx) == len(invs["nr"]):
            return rx
        # print(towers)
        # print()
    return numHigh, numLow


def part1(data):
    numHigh, numLow = sendSignal(data, 1)
    #print(f"High: {numHigh} Low: {numLow}")
    print(f"Part 1: {numHigh * numLow:_}")

def part2(data):
    rxs = sendSignal(data, 2)
    print(f"Part 2: {math.lcm(*rxs.values()):_}")

if __name__ == "__main__":
    data = parse()
    part1(data)
    part2(data)