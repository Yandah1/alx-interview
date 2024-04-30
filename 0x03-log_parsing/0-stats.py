#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""
import sys
from collections import defaultdict

# Initialize the cache to track status code counts
cache = defaultdict(int)

# Initialize variables for total size and line count
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        fields = line.split(" ")
        if len(fields) > 4:
            status_code = fields[-2]
            file_size = int(fields[-1])
        
            # Increment the count for the status code
            cache[status_code] += 1
        
            # Accumulate the total file size
            total_size += file_size
        
            # Increment the line count
            line_count += 1
        
            # Print metrics after every 10 lines
            if line_count % 10 == 0:
                print('Total file size:', total_size)
                for code, count in sorted(cache.items()):
                    if count > 0:
                        print(f'{code}: {count}')
                print()
                # Clear the cache for the next set of lines
                cache.clear()

except Exception as err:
    print('An error occurred:', err)

finally:
    # Print the final metrics
    print('Total file size:', total_size)
    for code, count in sorted(cache.items()):
        if count > 0:
            print(f'{code}: {count}')
