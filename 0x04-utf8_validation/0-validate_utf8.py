#!/usr/bin/python3
"""
Write a method that determines if a given data set
represents a valid UTF-8 encoding.

"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding
    or not
    Return: True if data is a valid UTF-8 encoding, else False.
    """

    byte_count = 0

    for i in data:
        if byte_count == 0:
            if i & 128 == 0:
                byte_count = 0
            elif i & 224 == 192:
                byte_count = 1
            elif i & 240 == 224:
                byte_count = 2
            elif i & 248 == 240:
                byte_count = 3
            else:
                return False
        else:
            if i & 192 != 128:
                return False
            byte_count -= 1

    return byte_count == 0
