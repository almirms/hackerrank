#!/usr/bin/python3
"""
https://www.hackerrank.com/challenges/minimum-distances
"""

array_size = int(input().strip())
numbers_array = [int(a_temp) for a_temp in input().strip().split(' ')]

array_size = len(numbers_array)
min_distance_found = array_size + 1
for i in range(0, array_size):
    for j in range(0, array_size):
        if numbers_array[i] == numbers_array[j]:
            abs_distance = abs(i - j)
            if i != j and abs_distance < min_distance_found:
                min_distance_found = abs_distance
if min_distance_found != array_size + 1:
    print(min_distance_found)
else:
    print(-1)
