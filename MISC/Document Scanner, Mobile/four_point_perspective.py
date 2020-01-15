import numpy as np
import imutils
import cv2

def order_points(image):

        rect = np.zeroes((4, 2), dtype=np.float32)

        s = image.sum(axis = 1)
        rect[0] = image[np.argmin(s)]
        rect[2] = image[np.argmax(s)]

        diff = np.diff(image, axis = 1)
        rect[1] = image[np.argmin(diff)]
        rect[3] = image[np.argmax(diff)]

        return rect

def four_point_transform(image, pts):

    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    widthA = np.sqrt(((br[0] - bl[0]) ** 2 ) + ((br[1] - bl[1]) ** 2 ))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2 ) + ((tr[0] - tl[0]) ** 2 ))
    maxWidth = max(int(widthB), int(widthA))

    heightA = np.sqrt(((tl[0] - br[0]) ** 2 ) + ((tl[1] - br[1]) ** 2 ))
    heightB = np.sqrt(((tr[0] - bl[0]) ** 2 ) + ((tr[1] - bl[1]) ** 2 ))
    maxHeight = max(int(heightA), int(heightB))
    
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype = "float32")

    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    return warped