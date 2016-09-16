#!/usr/bin/python3
"""
https://www.hackerrank.com/challenges/jumping-on-the-clouds
"""

quantity = int(input().strip())
path = list(input().split(' '))

location = 0
jumps = 0
while location != len(path) - 1:
    if location != len(path) - 2 and path[location + 2] == '0':
        location += 2
        jumps += 1
    else:
        location += 1
        jumps += 1
print(jumps)
