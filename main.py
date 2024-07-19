from m_tree import Tree
import time


idg = 0
N = 3
SIZE_OF_INPUT_DATA = 10
TEST_NAME = f"test_{SIZE_OF_INPUT_DATA}_nodes_test_{N}_M.txt" # название файла с данными


def get_sum_grans(node, data_sum=0):
    for _ in node.comm:
        if _ is not None:
            get_sum_grans(_, data_sum + node.data)
    node.data = data_sum


def print_tree(root, level=0, gee=2, deep=float('inf'), sign='────'):
    if not root:
        return
    if deep != 0:
        for _ in range(gee // 2):
            print_tree(root.comm[_], level + 1, gee, deep - 1, '┎───')
        print("    " * level + f"{sign}" + str(root.data))
        for _ in range(gee // 2, gee):
            print_tree(root.comm[_], level + 1, gee, deep - 1, "┖───")


tr = Tree(N)
start_time = time.time()

tr.read_tree_from_file(TEST_NAME)

end_time = time.time()
print('Gen time: ', end_time - start_time)
print_tree(tr.root, 0, N)

start_time = time.time()

get_sum_grans(tr.root)

end_time = time.time()
print('algo time: ', end_time - start_time)

print_tree(tr.root, 0, N)
