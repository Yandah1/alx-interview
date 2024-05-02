#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""


def parseLog():
    """
    Parses logs from standard input and calculates
    the file size and status codes.
    """
    import sys

    line_counter = 0
    total_size = 0
    status_counts = {'200': 0, '301': 0, '400': 0, '401': 0,
                     '403': 0, '404': 0, '405': 0, '500': 0}

    try:
        for line in sys.stdin:
            line_counter += 1
            line_list = line.split()
            try:
                size = int(line_list[-1])
                status_code = line_list[-2]

                if status_code in status_counts:
                    status_counts[status_code] += 1

                total_size += size
            except (IndexError, ValueError):
                pass

            if line_counter == 10:
                report(total_size, status_counts)
                line_counter = 0

        report(total_size, status_counts)

    except KeyboardInterrupt:
        report(total_size, status_counts)
        raise
    except BrokenPipeError:
        # Handle the BrokenPipeError explicitly
        pass


def report(total_size, status_counts):
    """
    Prints generated report to standard output
    Args:
        total_size (int): total log size after every 10 successfully read lines
        status_counts (dict): dictionary of status codes and counts
    """
    print("Total file size:", total_size)
    for code, count in sorted(status_counts.items()):
        if count != 0:
            print('{}: {}'.format(code, count))


if __name__ == '__main__':
    try:
        parseLog()
    except BrokenPipeError:
        pass
