#!/bin/python3

import math
import os
import random
import re
import sys

def maxTopics(a, b):
    # More readable solution, turning them into strings
    a_s = str(a)
    b_s = str(b)
    total_topics = 0
    for a_i, b_i in zip(a_s, b_s):
        if a_i == "1" or b_i == "1":
            total_topics += 1
    return total_topics

# Complete the acmTeam function below.
def acmTeam(topic):
    max_topics = None
    max_teams = None
    for i, contestant_a in enumerate(topic):
        for contestant_b in topic[i:]:
            max_topics_for_this_team = maxTopics(contestant_a, contestant_b)
            if max_topics is None or max_topics_for_this_team > max_topics:
                max_topics = max_topics_for_this_team
                max_teams = 1
            elif max_topics == max_topics_for_this_team:
                max_teams += 1
    return (max_topics, max_teams)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

