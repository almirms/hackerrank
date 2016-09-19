#!/usr/bin/python3
"""
https://www.hackerrank.com/challenges/pangrams
"""

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
            "y", "z"]

quote = input().strip().lower()

if all(x in quote for x in alphabet):
    print("pangram")
else:
    print("not pangram")
