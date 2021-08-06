#!/usr/bin/env python3
import sys, pyperclip

# Adds bullet points to the list on the clipboard

list = 'spam\nbacon\neggs' #pyperclip.paste()
lines = list.split('\n')

for i in range(len(lines)):
    lines[i] = f'* {lines[i]}'

list = '\n'.join(lines)
print(list)
