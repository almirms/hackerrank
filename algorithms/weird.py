#!/usr/bin/python3
"""
https://www.hackerrank.com/challenges/py-if-else
"""

n = int(input().strip())
if n % 2 != 0:
    print("Weird")
elif n in range(2, 6):
    print("Not Weird")
elif n in range(6, 21):
    print("Weird")
else:
    print("Not Weird")
