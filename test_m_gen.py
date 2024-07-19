import random
import sys
import math

sys.setrecursionlimit(100000000)


N = 10
HIGH_GEN = 100
DADS = 3
LOG = int(math.log(N, DADS))
count = 0


def gen_shit(deep=0, p=0):
    global count
    count += 1
    ids = count
    f.write(f'{random.randint(0, HIGH_GEN)} {p}\n')
    if count < N and deep <= LOG:
        for i in range(random.randint(DADS // 3, DADS)):
            gen_shit(deep + 1, ids)


f = open(f'test_{N}_nodes_test_{DADS}_M.txt', 'w')
gen_shit()
print(count, LOG)
f.close()
