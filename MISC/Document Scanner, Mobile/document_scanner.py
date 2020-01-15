pip install --upgrade skimage imutils cv2

from skimage.filters import threshold_local
from four_point_transform import four_point_transform
import cv2
import imutils
import argparse

ap = argparse.ArgumentParser()
ap.add('-i', "--image", required=True, "path for the image")

args = vars(ap.parse_args())

image = cv2.imread(args['image'])
ratio = image.shape[0] / 500.0
orig = image.copy()
image = imutils.resize(image, height = 500 )

# Convert the image into grayscale, blue ir, find edges, in the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3, 3), 0)
edged = cv2.Canny(gray, 75, 200)

# show the original image and the edge deteceted image
print("STEP 1: Edge Detection")
cv2.imshow("Image", image)
cv2.imshow("Edged", edged)
cv2.waitKey(0)
cv2.destroyAllWindows()

# find the contours in the Edged image, keeping only the
# largestones, and initialize the screen contour
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cv2.grabContours(cnts)

# Loop over the contours
for c in cnts:

    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)

    # If our aproximated contour has four points, then we
    # can assume that we ahe found our screen
    if len(approx) == 4:
        screenCnt = approx
        break
    
print("STEP 2: Find contours of paper")
cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
cv2.waitKey(0)
cv2.destroyAllWindows()