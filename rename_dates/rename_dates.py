#! python3
""" Rename files with emerican style dates to European style dates """

import shutil
import os
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))

date_pattern = re.compile(r"""^(.*?) # all text before the date
       ((0|1)?\d)-                  # one or two digits for the month
       ((0|1|2|3)?\d)-              # one or two digits for the day
       ((19|20)\d\d)                # four digits for the year
       (.*?)$                       # all text after the date
       """, re.VERBOSE)

for file in os.listdir('input'):
    match = date_pattern.fullmatch(file)
    if match is not None:
        groups = match.groups()
        prefix = groups[0]
        month = groups[1]
        day = groups[3]
        year = groups[5]
        suffix = groups[7]

        target_filename = f'{prefix}{day}-{month}-{year}-{suffix}'
        print(f'{file} -> {target_filename}')
        shutil.move(f'input/{file}', f'input/{target_filename}')
