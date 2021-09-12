#!/usr/bin/env python3

import shelve, pyperclip, sys

def usage():
    print('Usage: mcb.pyw [save [name]|list|key]')
    sys.exit(0)

if len(sys.argv) < 2:
    usage()

shelf = shelve.open('mcb')

command = sys.argv[1]
if len(sys.argv) == 3 and command == 'save':
    key = sys.argv[2]
    shelf[key] = pyperclip.paste()
    print(f'saved clipboard as {key}')
elif command == 'list':
    print(str(list(shelf.keys())))
elif command in shelf:
    pyperclip.copy(shelf[command])
    print(f'loaded {command}')
else:
    print(f'Unknown command or key {command}')

shelf.close()

