import cv2
import numpy as np
from core.image_loader import Loader

image_path = "C:\Users\isaul\Documents\image-processing-main\images\lenna.tiff"
loader = Loader(source=image_path).load()

image = loader.get_image()
cv2.imshow("Original", image)
