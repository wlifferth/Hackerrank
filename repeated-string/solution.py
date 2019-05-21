#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    counts = 0
    for c in s:
        if c == "a":
            counts += 1
    counts *= n // len(s)
    for c in s[:n % len(s)]:
        if c == "a":
            counts += 1
    return counts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

