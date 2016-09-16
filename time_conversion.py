#!/usr/bin/python3
"""
https://www.hackerrank.com/challenges/time-conversion
"""

time = input().strip()
if "PM" in time:
    time = time.replace("PM", "")
    time_splitted = time.split(":")

    hora = int(time_splitted[0])
    if hora != 12:
        time_splitted[0] = hora + 12
else:
    time = time.replace("AM", "")
    time_splitted = time.split(":")

    hora = int(time_splitted[0])
    if hora == 12:
        time_splitted[0] = "00"

print(':'.join(map(str, time_splitted)))





