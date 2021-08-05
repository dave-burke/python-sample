#!/usr/bin/env python3
import sys, pyperclip

# An insecure password manager

db = {
    'google': 'abc123',
    'facebook': '123abc',
}

if len(sys.argv) < 2:
    print('Usage: pw.py [account]')
    sys.exit(0)

account = sys.argv[1]
if account in db:
    pyperclip.copy(db[account])
    print(f'Password for {account} copied to the clipboard.')
else:
    print(f'No account {account} in db')

