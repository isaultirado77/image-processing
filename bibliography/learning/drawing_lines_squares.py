import numpy as np
import cv2 as cv

canvas = np.zeros((300, 300, 3), dtype = "uint8")

green = (0, 255, 0)
red = (0, 0, 255)
blue = (255, 0, 0)

# Lines
cv.line(canvas, (0, 0), (300, 300), green, 1)
cv.line(canvas, (300, 0), (0, 300), red, 3)

# Rectangles
cv.rectangle(canvas, (10, 10), (60, 60), green, 4)
cv.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv.rectangle(canvas, (200, 50), (225, 125), blue, -1)

cv.imshow("Figures", canvas)
cv.waitKey(0)
