#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    beautiful_count = 0
    for x in range(i, j + 1):
        if is_beautiful(x, k):
            beautiful_count += 1
    return beautiful_count

def is_beautiful(x, k):
    if (x - get_reverse(x)) % k == 0:
        return True

def get_reverse(x):
    return int(str(x)[::-1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()

