import copy
import networkx as nx

if __name__=="__main__":
    def parse():
        wires = {}
        for line in open("day25.txt", "r").readlines():
            line = line.replace('\n','').split(": ")
            conns = line[1].split(' ')
            wires.update({line[0]: set(conns)})
        return wires
    data = parse()
    # for wire in copy.deepcopy(data):
    #     for conn in data[wire]:
    #         if conn not in data:
    #             data[conn] = set()
    #         data[conn].update({wire})
    for wire in data:
        print(wire, data[wire])
    print()

    def part1(wires):
        G = nx.MultiGraph()
        for wire in wires:
            G.add_node(wire)
        for wire in wires:
            for con in wires[wire]:
                G.add_edge(wire, con)
        #print(len(nx.minimum_edge_cut(G)))
        G.remove_edges_from(nx.minimum_edge_cut(G))
        nx.connected_components(G)
        cycleLen = [len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]
        print(cycleLen)
        ans = 1
        for cLen in cycleLen:
            ans *= cLen
        print(f"Part 1: {ans}")
    part1(data)

