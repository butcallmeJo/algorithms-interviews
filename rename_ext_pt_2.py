import os

directory = os.listdir('.')

for file in directory:
    if file.endswith('txt'):
        basename = file.split('.')[:1:]
        os.rename(file, '.'.join(basename) + '.docx')