#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    inverse_indices = {}
    results = []
    for i in range(len(p)):
        inverse_indices[p[p[i] - 1] - 1] = i
    for i in range(len(p)):
        results.append(inverse_indices[i] + 1)
    return results



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

