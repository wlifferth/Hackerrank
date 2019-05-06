#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    set_size = defaultdict(lambda: 0)
    max_set_size = 0
    for ai in a:
        set_size[(ai - 1, ai)] += 1
        set_size[(ai, ai + 1)] += 1
    for k, v in set_size.items():
        if v > max_set_size:
            max_set_size = v
    return max_set_size

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
