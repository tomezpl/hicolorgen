#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys

print "Hicolor Icon Generator v0.1 by Tomasz Zając (c) 2016\n"

iconSrc = sys.argv[1]
iconRootDir = "//usr//share//icons//hicolor//"
availSizes = [16, 22, 24, 32, 36, 48, 64, 72, 96, 128, 192, 256, 512]

for size in availSizes:
	os.system(os.path.dirname(os.path.realpath(__file__)) + "/resize.py " + iconSrc + " " + os.path.splitext(iconRootDir + str(size) + "x" + str(size) + "//apps//" + os.path.basename(iconSrc))[0]+'.png' + " " + str(size) + " " + str(size))
os.system("gtk-update-icon-cache " + iconRootDir)