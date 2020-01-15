# couldn't get the image files because server wasn't loading. :/

pip install --upgrade skimage
pip install --upgrade imutils

from skimage.measure import compare_ssim
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add('-f', "--first", required=True, "1st image location")
ap.add('-s', "--second", required=true, "2nd image location")

# Extract the arugments sent from the CLI
args = vars(ap.parse_args())

# Store into local variables
imageA = cv2.imread(args['first'])
imageB = cv2.imread(args['second'])

# Convert to Gray scale, store in grayA and grayB
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

(score, diff) = compare_ssim(grayA, grayB, full=True)
diff = ( diff * 255 ).astype("uint8")
print("SSIM: {}".format(score))

thresh = cv2.threshold(diff, 255, cv2.BINARY_THRESH_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findCounters(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for c in cnts:

    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow("ImageA", imageA)
cv2.imshow("ImageB", imageB)
cv2.imshow("diff", diff)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)