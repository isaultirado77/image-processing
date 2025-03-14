import numpy as np
import cv2
from core import drawing

drawer = drawing.Drawer(width=300, height=300)

rectangle = drawer.rectangle(top_left=(25, 25),
                            bottom_right=(275, 275),
                            color=255,
                            thickness=-1)
rectangle.show(name="Rectangle")
