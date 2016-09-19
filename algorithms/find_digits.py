#!/usr/bin/python3
"""
https://www.hackerrank.com/challenges/find-digits
"""


def obtain_digits(number):
    return [int(x) for x in list(str(number))]


def quantity_divisible_numbers(number, dividends):
    count = 0
    for dividend in dividends:
        if dividend != 0 and number % dividend == 0:
            count += 1
    return count


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(quantity_divisible_numbers(n, obtain_digits(n)))
