#! /bin/env python3
""" Create incremental snapshots in zipfiles """

import os
import sys
import zipfile

if len(sys.argv) <= 1:
    print(f'Usage: {os.path.basename(__file__)} [dir to backup]')
    sys.exit(1)

input_dir = sys.argv[1]
if not os.path.isdir(input_dir):
    print('First arg must be a directory')
    sys.exit(1)

zip_basename = os.path.basename(input_dir)
increment = 0
for file in os.listdir(os.path.dirname(__file__)):
    if f'{zip_basename}_' in file:
        increment += 1
        print(f'Found {file}')

zip_filename=f'{zip_basename}_{increment}.zip'

print(f'Creating {zip_filename}')
backup_file = zipfile.ZipFile(zip_filename, 'w')
for folder, _, filenames in os.walk(input_dir):
    for filename in filenames:
        filepath = os.path.join(folder, filename)
        backup_file.write(filepath, compress_type=zipfile.ZIP_DEFLATED)
        info = backup_file.getinfo(filepath)
        if info.file_size == 0:
            ratio = 1.0
        else:
            ratio = round(info.compress_size / info.file_size, 2)
        print(f'Added {filepath} ({info.compress_size} / {info.file_size} = {ratio} ')

backup_file.close()
