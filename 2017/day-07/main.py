import re

with open('input.txt', 'r') as f:
    data_raw = f.readlines()

#  with open('input-sample.txt', 'r') as f:
    #  data_raw = f.readlines()

class Node:
    def __init__(self, raw):
        pattern_lhs = r'(\w+) \((\d+)\)'
        name, weight = re.findall(pattern_lhs, raw.strip())[0]
        self.name = name
        self.weight = int(weight)
        self.parent = None

        pattern_rhs = r'-> (.*)'

        if re.search(pattern_rhs, raw.strip()):
            children = re.findall(pattern_rhs, raw.strip())[0].split(',')
            self.children = [child.strip() for child in children]
        else:
            self.children = []

    def is_balanced(self):
        if self.children:
            child_weight = tree[self.children[0]].full_weight()
            return all(tree[child].full_weight() == child_weight for child in self.children)
        else:
            return True

    def full_weight(self):
        if self.children:
            return self.weight + sum(tree[child].full_weight() for child in self.children)
        else:
            return self.weight

    def __repr__(self):
        return f'{self.name} ({self.weight}) -> {self.children}'

nodes = [Node(i) for i in data_raw]
tree = {node.name: node for node in nodes}
for name, node in tree.items():
    for child in node.children:
        tree[child].parent = name

top_node = [name for name, n in tree.items() if n.parent is None][0]
print(f"TOP NODE: {top_node}")

bad_nodes = [node for name, node in tree.items() if not node.is_balanced()]
for node in bad_nodes:
    weights = [tree[child].full_weight() for child in node.children]
    print(f'{node.name} ::: {weights}')









