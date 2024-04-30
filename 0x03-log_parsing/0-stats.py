#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""
import sys
from collections import defaultdict

cache = defaultdict(int)
total_size = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])
            cache[code] += 1
            total_size += size

            if len(cache) == 10:
                print('File size: {}'.format(total_size))
                for key, value in sorted(cache.items()):
                    if value != 0:
                        print('{}: {}'.format(key, value))
                cache.clear()

except Exception as err:
    # Handle exceptions appropriately
    print("An error occurred:", err)

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
