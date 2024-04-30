#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""
import sys
import re
from collections import Counter


status_code_counts = Counter()
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line = line.strip()
        
        match = re.match(r'(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)', line)
        if not match:
            continue
        
        ip_address, date, status_code, file_size = match.groups()
        file_size = int(file_size)
        
        total_size += file_size
        status_code_counts[status_code] += 1
        line_count += 1
        
        if line_count % 10 == 0:
            print("Total file size:", total_size)
            for code, count in status_code_counts.items():
                print(f"{code}: {count}")
            print()
    
except KeyboardInterrupt:
    print("\nKeyboard Interrupt received. Exiting...")

print("Total file size:", total_size)
for code, count in status_code_counts.items():
    print(f"{code}: {count}")