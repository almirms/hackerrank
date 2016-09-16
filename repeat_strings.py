#!/usr/bin/python3
"""
https://www.hackerrank.com/challenges/repeated-string
"""

string = input().strip()
n = int(input().strip())
iters = int(n/len(string))

print((string.count("a") * iters) + string[0:n - (iters * len(string))].count("a"))
