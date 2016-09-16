#!/usr/bin/python3
"""
https://www.hackerrank.com/challenges/beautiful-binary-string
"""

s = input().strip()
changes = 0
while "010" in s:
    s = s.replace("010", "011", 1)
    changes += 1
print(changes)

