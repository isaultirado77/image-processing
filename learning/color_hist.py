import cv2
import numpy as np
import matplotlib.pyplot as plt
from core.image_loader import Loader

source = "monkey.tiff"

loader = Loader(source)
loader.load()

image = loader.get_image()
cv2.imshow("Monkey", image)

chans = cv2.split(image)
colors = ("b", "g", "r")
plt.figure()
plt.title("Flattened Color histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
for (chan, color) in zip(chans, colors): 
    hist = cv2.calcHist(images=[chan], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)