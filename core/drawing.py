import cv2
import numpy as np

class Drawing: 
    def __init__(self, width: int = 256, height: int = 256, background: tuple = (0, 0, 0)):
        """..."""
        self._canvas = np.zeros((height, width, 3), dtype="unit8")
        self._canvas[:] = background

    def line(self, start: tuple, end: tuple, color: tuple = (256, 256, 256), thickness: int = 1):
        """..."""
        cv2.line(self._canvas, start, end, color, thickness)

    def rectangle(self, top_left: tuple, bottom_right: tuple, color: tuple = (256, 256, 256), thickness: int = 1): 
        """..."""
        cv2.rectangle(self.canvas, top_left, bottom_right, color, thickness)

    def circle(self, center: tuple, radius: int, color: tuple = (256, 256, 256), thickness: int = 1):
        """...""" 
        cv2.circle(center, radius, color, thickness)

    def random_circle(self): 
        """..."""
        pass

    def elipse(self): 
        """..."""
        pass

    def polygon(self): 
        """..."""
        pass

    def text(self): 
        """..."""
        pass

    def show(self): 
        """..."""
        pass

    def save(self): 
        """..."""
        pass
