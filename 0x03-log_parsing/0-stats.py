#!/usr/bin/python3
""" Log parsing """


from sys import stdin


file_size = 0
line_count = 0
status_codes = 0

status_codes = {'200' : 0, '301' : 0, '400' : 0, '401' : 0, '403' : 0, '404' : 0, '405' : 0, '500' : 0 }

def print_stats(file_size, status_codes):
    for key, value in sorted(status_codes.items()):
        if value > 0:
            print('{}:{}'.format(key, value))


try:
    for line in stdin:
        line_count  += 1
        split_line = line.split()

        if len(split_line) > 1:
            file_size += int(split_line[-1])

        if len(split_line) > 2 and split_line[-2].isnumeric():
            status_code = split_line[-2]
        else:
            status_code = 0

        if status_code in status_codes.keys():
            status_codes[status_code] += 1

        if line_count  % 10 == 0:
            print_stats(file_size, status_codes)

    print_stats(file_size, status_codes)

except (KeyboardInterrupt):
    print_stats(file_size, status_codes)
    raise