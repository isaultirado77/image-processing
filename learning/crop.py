import cv2
import numpy as np
from core.image_loader import Loader

image_path = "lenna.tiff"
loader = Loader(image_path)
loader.load()

image = loader.get_image()
cv2.imshow("Original", image)
cv2.waitKey(0)