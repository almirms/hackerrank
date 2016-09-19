#!/usr/bin/python3
"""
https://www.hackerrank.com/challenges/camelcase
"""

import re

s = input().strip()
words = re.findall('[A-Z][a-z]*|[a-z][a-z]*', s)
print(len(words))
