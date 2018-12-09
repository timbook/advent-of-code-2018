class Node:
    def __init__(self, data):
        # Header
        self.n_children = data[0] if data else 0
        self.n_metadata = data[1] if data else 0

        # Child nodes
        self.children = []
        if self.n_children == 0:
            self.metadata = data[2:(2 + self.n_metadata)]
            self.body_size = 0
            self.size = 2 + self.n_metadata
        else:
            size_acc = 0
            for _ in range(self.n_children):
                ch = Node(data[2 + size_acc:])
                size_acc += ch.size
                self.children.append(ch)

            self.body_size = sum(ch.size for ch in self.children)
            self.size = 2 + self.body_size + self.n_metadata

        # Get metadata
        start_ind = 2 + self.body_size
        self.metadata = data[start_ind:(start_ind + self.n_metadata)]

    def sum_child_meta(self):
        if self.n_children == 0:
            return sum(self.metadata)
        else:
            sum_child_nodes = sum(ch.sum_child_meta() for ch in self.children)
            return sum(self.metadata) + sum_child_nodes

    def get_value(self):
        if self.n_children == 0:
            return sum(self.metadata)
        else:
            child_values  = 0
            for m in self.metadata:
                try:
                    child_values += self.children[m - 1].get_value()
                except:
                    pass
            return child_values
