import sys

sys.setrecursionlimit(100000000)


class Node:
    def __init__(self, data, n=2, parent_id=0):
        global idg
        self.parent_id = parent_id
        self.data = data
        self.ids = idg
        idg += 1
        self.comm = [None] * n

    def return_children(self, children_id):
        for _ in self.comm:
            if _.ids == children_id:
                return _

    def append(self, obj):
        for _ in range(len(self.comm)):
            if self.comm[_] is None:
                self.comm[_] = obj
                break


class Tree:
    def __init__(self, n):
        self.root = None
        self.n = n

    def find_parent_node(self, parent_id):
        parent_id -= 1
        if parent_id != 0:
            return self.find_parent_node(read_from_file_data[parent_id][1]).return_children(parent_id)
        else:
            return self.root

    def read_tree_from_file(self, file_name):
        global read_from_file_data
        read_from_file_data = list(map(lambda x: list(map(int, x.split())), open(file_name, 'r').read().split('\n')[:-1]))
        self.root = Node(read_from_file_data[0][0], self.n)
        for i in range(1, len(read_from_file_data)):
            self.find_parent_node(read_from_file_data[i][1]).append(Node(read_from_file_data[i][0], self.n, read_from_file_data[i][1]))


idg = 0
