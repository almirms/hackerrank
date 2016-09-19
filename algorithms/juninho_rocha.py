#!/usr/bin/python3
"""
https://www.hackerrank.com/challenges/gem-stones
"""

quantity = int(input().strip())
unique_elements = set((input().strip()))
for i in range(0, quantity - 1):
    unique_elements = unique_elements.intersection(set((input().strip())))

print(len(unique_elements))
