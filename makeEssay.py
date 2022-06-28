# makeEssay.py

# This script takes HTML files for the essay bodies and inserts them into the wrapper for all writings, so I don't have to do it by hand.


import re
import sys


DIR = "./writing/writingDirectory.html"

# Taken from maintenance/template.html
WRAPPER = '''
<!DOCTYPE html>
<html>
    <head>
        
        <title>Collisteru</title>
        <meta charset="UTF-8">
        <meta name="description" content=" {0} ">
        <meta name="author" content="Sean Carter">
        <link rel="stylesheet" type="text/css" href="../css/style.css" title="style"> 
    </head>
    <body>
        <div id="headbox">
                <a href="https://collisteru.github.io/index.html" class="headerLink" > <div><b>Collisteru</b></div></a> 
                <a href="https://collisteru.github.io/writing/writingDirectory.html" class="headerLink" > <div>Writing</div></a> 
                <a href="https://collisteru.github.io/contact.html" class="headerLink" > <div>Contact</div></a> 
            </div>
        <div class="upperScroll"> </div>
        <div id="mainbox">

        {1}

        </div>
        <div class="bottomScroll"> </div>
        <div class="earthWrapper">
            <img src="../art/earthInSpaceTwiceCropped.png">
        </div>
        

    </body>
</html>
'''


DIRENTRY = '''
                <!--{0}-->
                <tr>
                  <td><a href="{0}">{1}</a></td>
                  <td>{2}</td>
                </tr>
'''

class makeEssay():
    def __init__(self, essayBody, content="Collisteru"):
        self.essayBody = essayBody
        self.content = content


    def wrap(self):
        essay = WRAPPER
        re.sub('{0}', essay, content)
        re.sub('{1}', essay, essayBody)
        return essay

    # Adds the file information to the 'writings' directory
    def addToDir(self, essayAbbrev, essayTitle, essayDescription):
        # TODO: How to handle multi-word command line arguments?
        # {0} is the file URL (relative to the writing subdirectory, which shouldn't matter.
        # {1} is the title of the article as it will appear in the directory
        # {2} is a short description

        # We first modify DIRENTRY to make the custom entry we need
        myDirEntry = DIRENTRY
        fileURL = "./" + essayAbbrev + ".html"
        re.sub('{0}', myDirEntry, fileURL)
        re.sub('{1}', myDirEntry, essayTitle)
        re.sub('{2}', myDirEntry, essayDescription)

        # Next, we insert DIRENTRY into dir
        with open(DIR, 'r+') as masterDir:
            dirText = masterDir.read()
            re.sub('<!--{0}-->', dirText, myDirEntry)
            masterDir.write(dirText)

# TODO: Consider using argparse for this
# Argument 0: The file name, without extensions or prefixes
# Argument 1: The content heading to be displayed in the file's tab
# Argument 2: The full essay title
# Argument 3: A short description of the essay
if __name__ == "__main__":
    # Make essay body by wrapping up the essay in our CSS
    # Arguments are in sys.argv
    with open(SOURCE, 'r+') as src:
        body = src.read()
    fullEssay = makeEssay(body, sys.argv[1])
    wrappedBody = fullEssay.wrap()
    # Replace file contents with those of wrappedBody
    src.write(wrappedBody)

    # Add to directory
    fullEssay.addToDir(sys.argv[0], sys.arv[2], sys.argv[3])
