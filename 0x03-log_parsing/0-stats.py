#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""
import sys

status_counts = {'200': 0, '301': 0, '400': 0, '401': 0,
                 '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
line_counter = 0

try:
    for line in sys.stdin:
        line_list = line.split()
        if len(line_list) > 4:
            status_code = line_list[-2]
            size = int(line_list[-1])

            if status_code in status_counts:
                status_counts[status_code] += 1

            total_size += size
            line_counter += 1

        if line_counter == 10:
            line_counter = 0
            print('Total file size:', total_size)
            for code, count in sorted(status_counts.items()):
                if count != 0:
                    print('{}: {}'.format(code, count))
            print()

except Exception as err:
    print('An error occurred:', err)

finally:
    print('Total file size:', total_size)
    for code, count in sorted(status_counts.items()):
        if count != 0:
            print('{}: {}'.format(code, count))
