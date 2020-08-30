#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    total_moves = 0
    obstacle_set = set(obstacles)
    print(obstacle_set)
    for row_change in (-1, 0, 1):
        for col_change in (-1, 0, 1):
            if row_change != 0 or col_change != 0:
                current_r = r_q + row_change
                current_c = c_q + col_change
                while current_r > 0 and current_r <= n and current_c > 0 and current_c <= n and (current_r, current_c) not in obstacle_set:
                    print(current_r, ',', current_c)
                    total_moves += 1
                    current_r += row_change
                    current_c += col_change

    return total_moves

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(tuple(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()

