#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    deduped_scores = list()
    results = []
    for score in scores:
        if len(deduped_scores) == 0 or score != deduped_scores[-1]:
            deduped_scores.append(score)
    print(deduped_scores)
    leaderboard_index = len(deduped_scores) - 1
    for alice_score in alice:
        while leaderboard_index > -1 and alice_score > deduped_scores[leaderboard_index]:
            leaderboard_index -= 1
        # If we have a tie with the current leaderboard_index we're one place better
        if deduped_scores[leaderboard_index] == alice_score:
            results.append(leaderboard_index + 1)
        else:
            results.append(leaderboard_index + 2)
    print(results)
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

