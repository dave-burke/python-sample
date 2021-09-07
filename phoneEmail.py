#!/usr/bin/env python3
# Find phone numbers and email addresses on the clipboard

import pyperclip
import re

phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))? # area code
        (\s|-|\.)? # separator
        (\d{3}) # first part
        (\s|-|\.) # separator
        (\d{4}) # second part
        (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
        [a-z.-_%+]+ # address
        @
        [a-z.-]+ # domain
        \.[a-z]{2,10} # tld
)''', re.VERBOSE | re.IGNORECASE)

#text = pyperclip.paste()
text = '''
123.456.7890
(123)456-7890
(123)456-7890 ext. 123
123-4567
123-4567 x3245
test@example.com
'''

for match in phoneRegex.findall(text):
    phone = '-'.join([match[1],match[3],match[5]])
    if match[8] != '':
        phone += match[8]
    print(phone)

for match in emailRegex.findall(text):
    print(match)

