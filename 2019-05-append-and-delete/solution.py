#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    # get the common prefix
    i = 0
    while s[i] == t[i]:
        i += 1
        if i >= len(s) or i >= len(t):
            break
    ops_needed = (len(s) + len(t) - (2 * i))
    if ops_needed > k:
        return "No"
    elif (len(s) + len(t) > k) and (ops_needed - k) % 2 != 0:
        # The rare case that we have more operations that we need, we can't sink them            # into "deleting the empty string" and we have an odd number of excess ops
        return "No"
    else:
        return "Yes"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()

