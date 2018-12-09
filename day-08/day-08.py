from node import Node

with open("../data/08-input.txt") as f:
    data = f.read().split(' ')

data = [int(datum) for datum in data]

root = Node(data)
sum_meta = root.sum_child_meta()

print("::: PART A")
print(f"The sum of all meta data: {sum_meta}\n")

#==============================================================================

print("::: PART B")
print(f"The value of the root node: {root.get_value()}")
