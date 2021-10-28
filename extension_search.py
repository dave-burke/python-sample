#!/bin/env python3
""" Find all files with a given extension in a source dir and copy them to a dest dir """

import os
import shutil
import sys

if len(sys.argv) != 4:
    print(f'Usage: {os.path.basename(sys.argv[0])} [ext] [source_dir] [dest_dir]')
    sys.exit(1)

ext,source_dir,dest_dir = sys.argv[1:4]

if not os.path.isdir(source_dir):
    print(f'{source_dir} is not a directory. 2nd arg must be a directory.')

if not os.path.isdir(dest_dir):
    print(f'{dest_dir} is not a directory. 3rd arg must be a directory.')

if not ext.startswith('.'):
    ext = '.' + ext

source_dir = os.path.abspath(source_dir)
dest_dir = os.path.abspath(dest_dir)

print(f'Copying {ext} files from {source_dir} into {dest_dir}')

for dirname,_,filenames in os.walk(source_dir):
    for filename in filenames:
        if filename.endswith(ext):
            source_file = os.path.abspath(os.path.join(dirname, filename))
            print(f'Copying {source_file} to {dest_dir}')
            #shutil.copy(source_file, dest_dir)
