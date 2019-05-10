#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    SPRING = 0
    SUMMER = 1
    season = SPRING
    height = 1
    for i in range(n):
        if season == SPRING:
            height *= 2
            season = SUMMER
        elif season == SUMMER:
            height += 1
            season = SPRING
    return height

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()

