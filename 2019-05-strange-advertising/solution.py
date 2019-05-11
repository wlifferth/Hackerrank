#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    cumulitive_likes = 0
    recipients = 5
    for i in range(n):
        likes_this_round = math.floor(recipients / 2)
        recipients_next_round = likes_this_round * 3
        cumulitive_likes += likes_this_round
        recipients = recipients_next_round
    return cumulitive_likes


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

