# MAKEFILE

testWrap:
	./wrap.py ./writing/testText.html testing... TEST TESTDSCRPT

# UNBUILT
# TODO: Consider using argparse for this
# Argument 0: The command name (./addToDir.py)
# Argument 1: The complete file name
# Argument 2: The content heading to be displayed in the file's tab
# Argument 3: The full essay title
# Argument 4: A short description of the essay

testAddToDir:
	./addToDir.py ./writing/testText.html  testing... ASIMPLETEST TESTDSCRPT

essay:
	./wrap.py $(filepath) $(heading) $(title) $(description)
	./addToDir.py $(filepath) $(heading) $(title) $(description)


help:
	echo essay filepath=FILEPATH heading=HEADING title=TITLE description=DESCRIPTION
