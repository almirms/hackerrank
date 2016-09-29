#!/usr/bin/python3
"""
https://www.hackerrank.com/challenges/circular-array-rotation
"""
from collections import deque


def rotate(list_to_rotate, rotations):
    d = deque(list_to_rotate)
    d.rotate(rotations)
    return list(d)


n_r_q = [int(x) for x in list(input().split(' '))]
n = n_r_q[0]
r = n_r_q[1]
q = n_r_q[2]

array = [int(x) for x in list(input().split(' '))]
r_array = rotate(array, r)
for query in range(0, q):
    print(r_array[int(input())])
