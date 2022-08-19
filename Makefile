# BLOG/COLLISTERU.GITHUB.IO/MAKEFILE
addToDir:
	./addToDir.py $(filepath) $(heading) $(title) $(description)

update:
	# Updates file that's already been indexed (for revising old essays)
	# filepath1 is the file to be replaced, filepath2 is the file that'll be doing the replacing
	cp $(filepath2) $(filepath1)

update_help:
	echo filepath1 is the file to be replaced, filepath2 is the file that will replace
	echo update filepath1=FILEPATH filepath2=FILEPATH2 heading=HEADING title=TITLE description=DESCRIPTION

help:
	echo "addToDir filepath heading title description"
