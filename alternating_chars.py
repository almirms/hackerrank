#!/usr/bin/python3
"""
https://www.hackerrank.com/challenges/alternating-characters
"""


def changes_made(param):
    if "A" in param and "B" in param:
        changes = 0
        while "AA" in param:
            changes += param.count("AA")
            param = param.replace("AA", "A")
        while "BB" in param:
            changes += param.count("BB")
            param = param.replace("BB", "B")
        return changes
    else:
        return len(param) - 1

quantity = int(input().strip())
for i in range(0, quantity):
    print(changes_made(input().strip()))
