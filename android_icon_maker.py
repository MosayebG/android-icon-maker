#!/usr/bin/python
import os, sys
import Image
import glob
from sys import *

icons = glob.glob("*.png")
sizes = [(192, 192), (144, 144), (96, 96), (72, 72), (48, 48)]
folders = ["xxxhdpi","xxhdpi", "xhdpi", "hdpi", "mdpi"]

for i in icons:
	for index in range(0,5):
		im = Image.open(i).convert("RGBA")
		im.thumbnail(sizes[index], Image.ANTIALIAS)
		im.save(folders[index] + "/" + i, "PNG")
