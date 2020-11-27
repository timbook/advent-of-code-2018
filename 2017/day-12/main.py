import re
import networkx as nx

with open('input.txt', 'r') as f:
    raw = f.read()
    raw = [line for line in raw.strip().split('\n')]

class Village:
    def __init__(self, raw):
        self.G = nx.Graph()
        self.process_input(raw)

    def process_input(self, raw):
        for line in raw:
            this_node, other_nodes = re.findall('(\d+) <-> (.*)', line)[0]

            other_nodes = other_nodes.split(', ')

            for other in other_nodes:
                self.G.add_edge(this_node, other)

    def n_in_group(self, origin):
        return len(nx.descendants(self.G, origin)) + 1

    def n_groups(self):
        n_groups = 0
        nodes_remaining = set(self.G.nodes)

        while nodes_remaining:
            elem = min(nodes_remaining)
            group = nx.descendants(self.G, elem)
            group.add(elem)
            n_groups += 1
            nodes_remaining -= group

        return n_groups

v = Village(raw)
n_in_group = v.n_in_group('0')
print(f"There are {n_in_group} nodes in 0's group")

n_groups = v.n_groups()
print(f"There are {n_groups} total groups")
