import copy

if __name__=="__main__":
    def parse():
        wires = {}
        for line in open("day25.txt", "r").readlines():
            line = line.replace('\n','').split(": ")
            conns = line[1].split(' ')
            wires.update({line[0]: set(conns)})
        return wires
    data = parse()
    for wire in copy.deepcopy(data):
        for conn in data[wire]:
            if conn not in data:
                data[conn] = set()
            data[conn].update({wire})
    for wire in data:
        print(wire, data[wire])
    print()

    def part1(wires):
        # conns = []
        # for wire in wires:
        #     cons = wires[wire]
        #     for con in cons:
        #         if (wire,con) not in conns and (con,wire) not in conns:
        #             conns.append((wire,con))
        # print(len(conns))
        # print(conns)
        similarities = {}
        potents = set()
        for wire in wires:
            conns = wires[wire]
            similarities[wire] = set()
            for conn in conns:
                numSim = 0
                aConns = wires[conn]
                for aConn in aConns:
                    if aConn in conns:
                        numSim +=1
                similarities[wire].update({(conn, numSim)})
                if numSim == 0:
                    if (wire,conn) not in potents and (conn, wire) not in potents:
                        potents.update({(wire, conn)})
        for wire in similarities:
            print(wire, similarities[wire])
        print()
        print(len(potents))
        print(potents)


    part1(data)

