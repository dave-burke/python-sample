#!/usr/bin/env python3
""" A regex-based reimplementation of 'strip' (for practice) """

import re
import sys

def strip(string, chars = None):
    """ Remove leading and trailing whitespace """
    if chars is None:
        regex = re.compile(r'^\s*(.*?)\s*$')
    else:
        regex = re.compile('^[' + chars + ']*(.*?)[' + chars + ']*$')
    match = regex.search(string)
    return match.group(1)

if len(sys.argv) == 1:
    print("At least one arg is required")
    sys.exit(1)
elif len(sys.argv) == 2:
    result = strip(sys.argv[1])
elif len(sys.argv) == 3:
    result = strip(sys.argv[1], sys.argv[2])

print(f'"{result}"')
