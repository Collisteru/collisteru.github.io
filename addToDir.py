#!/usr/bin/env python
# addToDir.py


from trimmer import *

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
    fullEssay = trimmer(body, sys.argv[2])
    fullEssay.addToDir(sys.argv[1], sys.argv[3], sys.argv[4])
