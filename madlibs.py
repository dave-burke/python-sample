#!/usr/bin/env python3

""" Parse a madlibs file, prompt the user, and print the result """

import os, sys, re

def usage():
    print('Usage: madlibs.py [template file]')
    sys.exit(1)

if len(sys.argv) < 2 or not os.path.exists(sys.argv[1]):
    usage()

file = open(sys.argv[1], 'r')
try:
    text = file.read()
    wordRegex = re.compile(r'ADJECTIVE|VERB|NOUN|ADVERB')
    match = wordRegex.search(text)
    while match is not None:
        word = input(f'Give me a {match.group()}: ')
        text = text.replace(match.group(), word, 1)
        match = wordRegex.search(text)
    print(text)
finally:
    file.close()

