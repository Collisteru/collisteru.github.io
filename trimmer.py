#!/usr/bin/env python
# trimmer.py

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
                <!--{7}-->
                <tr>
                  <td><a href="{0}">{1}</a></td>
                  <td>{2}</td>
                </tr>
'''

class trimmer():
    def __init__(self, essayBody, content="Collisteru"):
        self.essayBody = essayBody
        self.content = content

    # DIR is the file URL (relative to the writing subdirectory, which shouldn't matter.)
    def getContent(self, DIR):
        with open(DIR, 'r+') as masterDir:
            dirText = masterDir.read()
            # Testing functions is a good idea!
            return dirText

    # Content is the small description that will appear at the top of the tab.
    # EssayBody is the actual text of the essay
    def wrap(self):
        essay = WRAPPER
        # NOTHING TO REPEAT
        # re.sub: To see, to replace, withinThis
        testSub = re.sub('(e)', 'i', 'hello')
        essay = re.sub('\{0\}', self.content, essay)
        essay = re.sub('\{1\}', self.essayBody, essay)
        return essay

    # Adds the file information to the 'writings' directory
    # TODO: How to handle multi-word command line arguments?
    # fileURL is the file URL (relative to the writing subdirectory, which shouldn't matter.
    # essayTitle is the title of the article as it will appear in the directory
    # essayDescription is a short description
    def addToDir(self, fileURL, essayTitle, essayDescription):
        # We first modify DIRENTRY to make the custom entry we need
        myDirEntry = DIRENTRY
        myFileURL = re.sub('writing/', '', fileURL)
        myDirEntry = re.sub('\{0\}', myFileURL, myDirEntry)
        myDirEntry = re.sub('\{1\}', essayTitle, myDirEntry)
        myDirEntry = re.sub('\{2\}', essayDescription, myDirEntry)
        # Next, we insert DIRENTRY into dir
        with open(DIR, 'r+') as masterDir:
            dirText = masterDir.read()
            dirText = re.sub('<!--\{7\}-->', myDirEntry, dirText)
            masterDir.seek(0)
            masterDir.truncate()
            masterDir.write(dirText)
