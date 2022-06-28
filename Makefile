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

wrap:
	./wrap.py $(filepath) $(heading) $(title) $(description)

addToDir:
	./addToDir.py $(filepath) $(heading) $(title) $(description)

update:
	# Updates file that's already been indexed (for revising old essays)
	# filepath1 is the file to be replaced, filepath2 is the file that'll be doing the replacing
	cp $(filepath2) $(filepath1)
	./wrap.py $(filepath1) $(heading) $(title) $(description)

update_help:
	echo filepath1 is the file to be replaced, filepath2 is the file that will replace
	echo update filepath1=FILEPATH filepath2=FILEPATH2 heading=HEADING title=TITLE description=DESCRIPTION

help:
	echo essay filepath=FILEPATH heading=HEADING title=TITLE description=DESCRIPTION
