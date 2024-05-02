#!/usr/bin/python3
"""Script that reads stdin
"""


def parseLogs():
    """
    Parses logs from standard input and calculates
    the file size and status codes.

    """
    stdin = __import__('sys').stdin
    line_counter = 0
    fileSize = 0
    status_counts = {}
    codes = ('200', '301', '400', '401', '403', '404', '405', '500')
    try:
        for line in stdin:
            line_counter += 1
            line = line.split()
            try:
                fileSize += int(line[-1])
                if line[-2] in codes:
                    try:
                        status_counts[line[-2]] += 1
                    except KeyError:
                        status_counts[line[-2]] = 1
            except (IndexError, ValueError):
                pass
            if line_counter == 10:
                report(fileSize, status_counts)
                line_counter = 0
        report(fileSize, status_counts)
    except KeyboardInterrupt as e:
        report(fileSize, status_counts)
        raise
    except BrokenPipeError:
        # Handle the BrokenPipeError explicitly
        pass


def report(fileSize, status_counts):
    """
    Prints generated report to standard output
    Args:
        fileSize (int): total log size after every 10 successfully read line
        statusCodes (dict): dictionary of status codes and counts
    """
    print("File size: {}".format(fileSize))
    for key, value in sorted(status_counts.items()):
        print("{}: {}".format(key, value))


if __name__ == '__main__':
    try:
        parseLogs()
    except BrokenPipeError:
        # Handle the BrokenPipeError at the top level
        pass