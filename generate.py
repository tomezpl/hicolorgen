#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
import cv2
import numpy as np

print cv2.__version__

print "Hicolor Icon Generator v0.1 by Tomasz Zając (c) 2016\n"

iconSrc = sys.argv[1]
iconRootDir = "//usr//share//icons//hicolor//"
availSizes = [16, 22, 24, 32, 36, 48, 64, 72, 96, 128, 192, 256, 512]

"""for size in availSizes:
	os.system(os.path.dirname(os.path.realpath(__file__)) + "/resize.py " + iconSrc + " " + os.path.splitext(iconRootDir + str(size) + "x" + str(size) + "//apps//" + os.path.basename(iconSrc))[0]+'.png' + " " + str(size) + " " + str(size))
os.system("gtk-update-icon-cache " + iconRootDir)"""

img = cv2.imread(iconSrc, -1)

for size in availSizes:
	width = size / float(np.size(img, 0))
	height = size / float(np.size(img, 1))
	print "Resizing to ", size, "x", size, "..."
	res = cv2.resize(img, None, fx=width, fy=height, interpolation = cv2.INTER_CUBIC)
	print "Creating output icon file path..."
	finalpath = os.path.splitext(iconRootDir + str(size) + "x" + str(size) + "//apps//" + os.path.basename(iconSrc))[0] + '.png'
	print "Writing icon file to ", finalpath
	cv2.imwrite(finalpath, res)