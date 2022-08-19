#!/usr/bin/env python
# addToDir.py


import addToDir
import sys
import regex as re

# TODO: Consider using argparse for this
# Argument 0: The command name (./addToDir.py)
# Argument 1: The complete file name
# Argument 2: The content heading to be displayed in the file's tab
# Argument 3: The full essay title
# Argument 4: A short description of the essay

# def addToDir(self, essayAbbrev, essayTitle, essayDescription):
    # Adds the file information to the 'writings' directory
    # TODO: How to handle multi-word command line arguments?
    # fileURL is the file URL (relative to the writing subdirectory, which shouldn't matter.
    # essayTitle is the title of the article as it will appear in the directory
    # essayDescription is a short description
if __name__ == "__main__":
    # Add to directory
    with open(sys.argv[1], 'r+') as src:
        body = src.read()
    fullEssay = body
    fullEssay.addToDir(sys.argv[1], sys.argv[3], sys.argv[4])


    # We use underscores to separate words in the command line. Replace them with spaces for HTML insertion
    arg1 = re.sub("_", " ", sys.argv[1])
    arg2 = re.sub("_", " ", sys.argv[2])
    arg3 = re.sub("_", " ", sys.argv[3])
    arg4 = re.sub("_", " ", sys.argv[4])



    with open(arg1, 'r+') as src:
        body = src.read()
    fullEssay = trimmer(body, arg2)
    fullEssay.addToDir(arg1, arg3, arg4)
