#!/usr/bin/env python3
# WRAP.PY
# This script automatically wraps pages in the CSS above and below the main text of the website.


# TODO: Importing everything like this probably isn't the ideal solution; consider doing something else if you can.
from trimmer import *

# TODO: Consider using argparse for this
# Argument 0: The full file name
# Argument 1: The content heading to be displayed in the file's tab
# Argument 2: The full essay title
# Argument 3: A short description of the essay


# ./wrap.py testText.html testing... TEST TESTDSCRPT
if __name__ == "__main__":
#     print("sys.argv[0]: ", sys.argv[0]) # ./wrap.py
#     print("sys.argv[1]: ", sys.argv[1]) # testText.html
#     print("sys.argv[2]: ", sys.argv[2]) # testing...
#     print("sys.argv[3]: ", sys.argv[3]) # TEST
#     print("sys.argv[4]: ", sys.argv[4]) # TESTDSCRPT
    with open(sys.argv[1], 'r+') as src:
        body = src.read()
    # trimmer(essayBody=melvil.read(), content=testing...)
    fullEssay = trimmer(body, sys.argv[2])
    content = fullEssay.getContent(sys.argv[1])
    # Raise nothing to repeat for the below line
    wrappedBody = fullEssay.wrap()
    print("wrappedBody:\n ", wrappedBody)
    with open(sys.argv[1], 'r+') as src:
        body = src.write(wrappedBody)
