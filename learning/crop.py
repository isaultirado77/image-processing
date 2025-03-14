import cv2
import numpy as np
from core.image_loader import Loader

# source = "https://pesdb.net/pes2020/images/players/7511.png"
# source = r"C:\Users\isaul\Downloads\Jaguar - Ian Ford.jpeg"
source = "lenna.tiff"

loader = Loader(source)
loader.load()

image = loader.get_image()
cv2.imshow("Original", image)

cropped = image[220:400, 100:400]
cv2.imshow("Cropped", cropped)
cv2.waitKey(0)