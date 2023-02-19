#!/usr/bin/python3
"""
reads stdin line by line and computes metrix
"""

import sys

file_size = 0
counter = 0
s_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}


def print_stats(s_codes, file_size):
    """
    prints computed metrics
    """
    print("File size: {}".format(file_size))
    for key, value in sorted(s_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))


try:
    for line in sys.stdin:
        line_pas = line.split(" ")
        if len(line_pas) > 4:
            code = line_pas[-2]
            filesize = int(line_pas[-1])
            file_size += filesize
            counter += 1
            if code in s_codes.keys():
                s_codes[code] += 1
        if counter == 10:
            counter = 0
            print_stats(s_codes, file_size)
finally:
    print_stats(s_codes, file_size)
