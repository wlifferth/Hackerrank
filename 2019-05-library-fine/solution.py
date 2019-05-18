#!/bin/python3

import math
import os
import random
import re
import sys
import datetime

# Complete the libraryFine function below.
def libraryFine(d1, m1, y1, d2, m2, y2):
    date1 = datetime.date(day=d1, month=m1, year=y1)
    date2 = datetime.date(day=d2, month=m2, year=y2)
    if date1 < date2:
        return 0
    elif date1.year == date2.year and date1.month == date2.month:
        return 15 * (date1.day - date2.day)
    elif date1.year == date2.year and date1.month != date2.month:
        return 500 * (date1.month - date2.month)
    else:
        return 10000

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d1M1Y1 = input().split()

    d1 = int(d1M1Y1[0])

    m1 = int(d1M1Y1[1])

    y1 = int(d1M1Y1[2])

    d2M2Y2 = input().split()

    d2 = int(d2M2Y2[0])

    m2 = int(d2M2Y2[1])

    y2 = int(d2M2Y2[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()

