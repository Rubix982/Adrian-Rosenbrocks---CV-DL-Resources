import numpy as np
import argparse
import imutils
import cv2
import matplotlib.pyplot as plt

ap = argparse.ArgumentParser("Give path to the image")
ap.add_argument('-i', "--image", required=True, help="give path for the image")

args = vars(ap.parse_args())

image = cv2.imread(args['image'])

# for i in range(0, 360, 15):

#     tmp_img = imutils.rotate(image, i)
#     cv2.imshow("Rotated img", tmp_img)
#     cv2.waitKey(0)

# for i in range(0, 360, 15):
#     tmp_img = imutils.rotate_bound(image, i)
#     cv2.imshow("Rotated img (fixed)", tmp_img)
#     cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

for i in range(1, 19, 1):
    blur = cv2.GaussianBlur(gray, (i, i), 0)
    cv2.imshow("Rotated", blur)
    cv2.waitKey(0)