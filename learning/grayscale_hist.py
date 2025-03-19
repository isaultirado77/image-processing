import cv2
import numpy as np
import matplotlib.pyplot as plt
from core.image_loader import Loader

source = "lenna.tiff"

loader = Loader(source)
loader.load()

image = loader.get_image()
cv2.imshow("Original", image)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray_image)

hist = cv2.calcHist(images=gray_image, channels=[0], mask=None, histSize=[256], ranges=[0, 256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)
