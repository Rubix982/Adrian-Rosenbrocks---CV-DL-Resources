# Article at, https://www.pyimagesearch.com/2015/04/20/sorting-contours-using-python-and-opencv/

import numpy as np
import argparse
import imutils
import cv2

def sort_contours(cnts, method="left-to-right"):

    # initialize the reverse flag and sort index
    reverse = False
    i = 0

    # handle if we need to sort in reverse
    if method == "left-to-right" or method == 'bottom-to-top':
        reverse = True

    # handle if we are sorting against the y-coordinates, other than
    # the x-coordinate of the bounding box
    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1

    # construct the list of bounding boxes and sort them from top to
    # bottom
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip( *sorted(zip(cnts, boundingBoxes),
        key=lambda b:b[1][i], reverse=reverse) )

    # return the lsit of sorted contours and bounding boxes
    return (cnts, boundingBoxes)

def draw_contours(image, c, i):

    # compute the center of the contour area and draw a circle
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])

    # draw the contour number on the image
    cv2.putText(image, "#{}".format(i + 1), (cX - 20, cY), cv2.FONT_HERSHEY_SIMPLEX,
        1.0, (255, 255, 255), 2)
    
    # return the image with the contour number draw on
    return image