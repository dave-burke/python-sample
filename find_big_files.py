#!/bin/env python3
""" Find files larger than the given size (in MB) in the given dir """

import os
import sys

if len(sys.argv) != 3:
    print(f'Usage: {__file__} [size in MB] [dir]')
    sys.exit(1)

size, dir = sys.argv[1:3]

if size.isnumeric():
    size = float(size)
else:
    print(f'First arg must be a number. {sys.argv[1]} is not')
    sys.exit(1)

if os.path.isdir(dir):
    dir = os.path.abspath(dir)
else:
    print(f'Second arg must be a directory. {dir} is not')
    sys.exit(1)

print(f'Finding files larger than {size}MB in {dir}')
for dir, _, filenames in os.walk(dir):
    for filename in filenames:
        absfile = os.path.abspath(os.path.join(dir, filename))
        file_size = os.path.getsize(absfile)
        file_size = round(file_size / 1000, 1)
        if file_size > size:
            print(f'{str(file_size).ljust(10)} {absfile}')
