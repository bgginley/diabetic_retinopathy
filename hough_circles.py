#!/usr/bin/env python3

#import necessary packages
import cv2
import numpy as np
import argparse
import copy
from PIL import Image
#construct argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help= "Path to the image")
args = vars(ap.parse_args())

#load the image, clone it for output, and convert to grayscale
image = cv2.imread(args["image"])
y = copy.copy(image)
gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#detect circles in the image
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)

#ensure at least some circles were found
if circles is not None:
	#convert the (x,y) coordinates and radius of the circles
	circles = np.round(circles[0, :]).astype("int")

	#loop over the (x,y) coordinates and radius of the circles 
	for (x,y,r) in circles:
		#draw the circle in the output image, then draw a rectangle
		#corresponding to the center of the circle
		tmp = np.hstack([image, y])
		img = Image.fromarray(np.hstack([image, y]), 'RGB')
		cv2.imshow("y", img)
		cv2.waitKey(0)
	
