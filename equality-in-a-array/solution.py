#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    counts = dict()
    max_count = 0
    for x in arr:
        if x not in counts:
            counts[x] = 0
        counts[x] += 1
        if counts[x] > max_count:
            max_count = counts[x]
    return len(arr) - max_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

