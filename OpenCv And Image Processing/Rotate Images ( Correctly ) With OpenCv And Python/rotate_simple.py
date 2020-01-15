import numpy as np
import argparse
import imutils
import cv2
import matplotlib.pyplot as plt

ap = argparse.ArgumentParser("Give path to the image")
ap.add_argument('-i', "--image", required=True, help="give path for the image")

args = vars(ap.parse_args())

image = cv2.imread(args['image'])

'''

Uncomment the below lines to see the images
being rotated, with unbounded and bounded

# for i in range(0, 360, 15):

#     tmp_img = imutils.rotate(image, i)
#     cv2.imshow("Rotated img", tmp_img)
#     cv2.waitKey(0)

# for i in range(0, 360, 15):
#     tmp_img = imutils.rotate_bound(image, i)
#     cv2.imshow("Rotated img (fixed)", tmp_img)
#     cv2.waitKey(0)

'''

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3, 3), 0)
edged = cv2.Canny(blue, 20, 100)
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

if len(cnts) > 0:

    c = max(cnts, key=cv2.contourArea)

    mask = np.zeroes(gray.shape, dtype="uint8")
    cv2.drawContours(mask, [c], -1, 255, -1)

    (x , y, w, h) = cv2.boundingRect(c)
    imageROI = image[y:y + h, x:x + w]
    maskROI = mask[y:y + h, x:x + w]
    imageROI = cv2.bitwise_and(imageROI, imageROI, mask=maskROI)

    for i in range(0, 360, 15):
        tmp_img = imutils.rotate(imageROI, i)
        cv2.imshow("Rotated img", tmp_img)
        cv2.waitKey(0)

    for i in range(0, 360, 15):
        tmp_img = imutils.rotate_bound(imageROI, i)
        cv2.imshow("Rotated img (fixed)", tmp_img)
        cv2.waitKey(0)
