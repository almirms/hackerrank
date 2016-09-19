#!/usr/bin/python3
"""
https://www.hackerrank.com/challenges/fibonacci-modified
"""

fibonaccis = [int(x) for x in list(input().split(' '))]
n = fibonaccis[2]

t0 = fibonaccis[0]
t1 = fibonaccis[1]
t2 = 0

count = 2
while count != n:
    t2 = t0 + (t1 ** 2)
    t0 = t1
    t1 = t2
    count += 1

print(t2)
