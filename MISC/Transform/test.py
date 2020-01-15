from four_point_transform import four_point_transform
import cv2
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('-i', "--image", required=True, "path to image" )
ap.add_argument('-c', "--cords" ,required=True, "coords to transform to")

args = vars(ap.parse_args())

image = cv2.imread(args['image']))

pts = np.array(eval(args['coords']), dtype=np.float32 )

warped = four_point_transform(image, pts)

cv2.imshow("Original", image)
cv2/imshow("Warped", warped)
cv2.waitKey(0)