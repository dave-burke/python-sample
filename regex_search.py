#!/usr/bin/env python

""" search all files in current dir for regex """

import re,os,sys

def usage():
    print(f'Usage: {sys.argv[0]} [regex]')
    sys.exit(0)

if len(sys.argv) == 1:
    usage()

regex = re.compile(sys.argv[1]) # Probably insecure
print(f'Searching for /{regex.pattern}/ in {os.getcwd()}')

files = os.listdir(os.getcwd())
for filename in files:
    if filename.endswith('.py'):
        try:
            file = open(filename, 'r')
            content = file.readlines()
            for line in content:
                match = regex.search(line)
                if match is not None:
                    print(f'{filename}:',line.replace(match.group(), f'*{match.group()}*'))
        finally:
            file.close()

