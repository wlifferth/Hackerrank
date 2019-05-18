#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    lens = []
    arr = sorted(arr)
    cut_length = 0
    i = 0
    while i < len(arr):
        lens.append(len(arr) - i)
        cut_length = arr[i]
        while i < len(arr) and arr[i] <= cut_length:
            i += 1
    return lens

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

