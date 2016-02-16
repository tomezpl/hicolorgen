#!/usr/bin/python
# -*- coding: utf-8 -*-

# Image resizer script
# Tomasz Zając (c) 2016
# This uses a bash script file (resize.sh) that contains the instructions 
# for a GIMP script that will resize the picture and save it under a new name.
# Please don't judge my Python skills, it's not that simple as C++. See what I did there?


import os, sys

shellScript = open(os.path.dirname(os.path.realpath(__file__)) + '//resize.sh', 'r')
shellCmd = shellScript.read()
shellScript.close()

srcPath = str.replace(sys.argv[1], " ", "\\ ") # Remove spaces if necessary - doesn't work
destPath = str.replace(sys.argv[2], " ", "\\ ")
newX = sys.argv[3]
newY = sys.argv[4]

shellCmd = shellCmd.replace("$PATH_TO_SRCIMG", srcPath)
shellCmd = shellCmd.replace("$PATH_TO_DESTIMG", destPath)
shellCmd = shellCmd.replace("$NEW_WIDTH", str(newX))
shellCmd = shellCmd.replace("$NEW_HEIGHT", str(newY))

print "This is the script:\n" + shellCmd + "\n\nExecuting now...\n\n"
os.popen(shellCmd, 'w', 0)