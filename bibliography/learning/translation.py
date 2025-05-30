import numpy as np
import argparse
import cv2


ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", required=True, help="Path to image. ")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Before", image)

M = np.float32([[1, 0, 25],[0, 1, 50]])

shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)

M = np.float32([[1, 0, -50], [0, 1, -90]])

shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Lefth", shifted)
cv2.waitKey(0)
