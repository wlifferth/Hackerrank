#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the nonDivisibleSubset function below.
def nonDivisibleSubset(k, S):
    remainder_counts = dict()
    selected_remainder_set = set()
    non_cohesive_sets = 0
    subset_count = 0
    for x in S:
        remainder = x % k
        if remainder not in remainder_counts:
            remainder_counts[remainder] = 0
        remainder_counts[remainder] += 1
    for remainder, count in remainder_counts.items():
        # If this remainder set added to itself is divisible by k, skip it
        if remainder * 2 == k and count > 1:
            non_cohesive_sets += 1
            continue
        if remainder == 0 and count > 1:
            non_cohesive_sets += 1
            continue
        if k - remainder not in remainder_counts:
            selected_remainder_set.add(remainder)
        elif remainder_counts[remainder] >= remainder_counts[k - remainder]:
            selected_remainder_set.add(remainder)
        else:
            selected_remainder_set.add(k - remainder)
    subset_count += non_cohesive_sets
    for remainder in selected_remainder_set:
        subset_count += remainder_counts[remainder]
    if subset_count == 0:
        return 1
    return subset_count





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    S = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, S)

    fptr.write(str(result) + '\n')

    fptr.close()

