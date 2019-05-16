#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    # First identify the lowest square higher than a
    lowest_sqaure_root = math.ceil(a ** 0.5)
    # Now identify the highest square lower than b
    highest_square_root = math.floor(b ** 0.5)
    # If the highest is lower than the lowest, there are no perfect squares in the range
    if lowest_sqaure_root > highest_square_root:
        return 0
    elif lowest_sqaure_root == highest_square_root:
        return 1
    else:
        return 1 + highest_square_root - lowest_sqaure_root

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()

