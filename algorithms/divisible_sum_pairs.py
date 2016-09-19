#!/usr/bin/python3
"""
https://www.hackerrank.com/challenges/divisible-sum-pairs
"""

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

pairs = list()
for i in range(0, len(a)):
    for j in range(0, len(a)):
        if i < j:
            pairs.append([a[i], a[j]])

count = 0
for pair in pairs:
    if (pair[0] + pair[1]) % k == 0:
        count += 1

print(count)
