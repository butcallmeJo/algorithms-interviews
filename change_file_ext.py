import os

'''
This program is dangerous and could change some files drastically. DO NOT RUN
unless you know what you are doing.

Change the file extension depending on DIRECTORY and FILE_EXT
'''

PATH = "/tmp/test/" # Specify path here
DIRECTORY = os.listdir(PATH) # List of files in dir
FILE_EXT = ".doc" # Specify which extension to replace by NEW_EXT
NEW_EXT = ".pdf" # Specify which extension to replace to

for filename in DIRECTORY: # Iterate over the list of filenames
    if filename.endswith(FILE_EXT): # If filename has the extension needed..
        no_ext = filename[:-(len(FILE_EXT))] # Gets the basename
        # print no_ext + NEW_EXT # To test what has been changed
        os.rename((PATH + filename), (PATH + no_ext + NEW_EXT)) # Renames file
