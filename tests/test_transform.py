import pytest 
import cv2
import numpy as np

from core.image_transform import ImageTransform
from core.image_loader import Loader

source = "lenna.tiff"
loader = Loader(source)
loader.load()
image = loader.get_image()

class TestTransfrorm: 
    pass