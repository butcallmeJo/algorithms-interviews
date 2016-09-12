import os

'''
This program is dangerous and could change some files drastically. DO NOT RUN unless you know what you are doing.
'''

directory = os.listdir('.') # looks inside current directory
ext_to_replace = 'doc' # replace this with whatever extension you want
new_ext = 'txt' # replace this with whatever extension you want

for file in directory:
    if file.endswith(ext_to_replace):
        basename = file.split('.')[:-1:] # splitting the full name at each '.' and not keeping track of the last 'extension' 
        os.rename(file, '.'.join(basename) + '.' + new_ext) # renames files from original to new concatenated version
