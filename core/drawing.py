import cv2
import numpy as np

class Drawing: 
    def __init__(self, width=255, height=255, background=(0, 0, 0)):
        """..."""
        self._canvas = np.zeros((height, width, 3), dtype="unit8")
        self._canvas[:] = background

    def line(self, start: tuple, end: tuple, color=(255, 255, 255), thickness=1):
        """..."""
        cv2.line(self._canvas, start, end, color, thickness)

    def rectangle(self, top_left: tuple, bottom_right: tuple, color=(255, 255, 255), thickness=1): 
        """..."""
        cv2.rectangle(self.canvas, top_left, bottom_right, color, thickness)

    def circle(self, center: tuple, radius: int, color=(255, 255, 255), thickness=1):
        """...""" 
        cv2.circle(center, radius, color, thickness)

    def random_circle(self): 
        """..."""
        pass

    def elipse(self): 
        """..."""
        pass

    def polygon(self, points: tuple, color=(255, 255, 255), thickness=1): 
        """..."""
        pts = np.array(points, np.int32).reshape((-1, 1, 2))
        cv2.polylines(self._canvas, [pts], isClosed=True, color=color, thickness=thickness)

    def text(self, text: str, position: tuple, font_scale=1, color=(255, 255, 255), thickness=2): 
        """..."""
        cv2.putText(self._canvas, text, position, cv2.FONT_HERSHEY_PLAIN, font_scale, color, thickness)

    def show(self, name="Drawing"): 
        """..."""
        cv2.imshow(mat=self._canvas, winname=name)
        cv2.imshow(0)
        cv2.destroyAllWindows()

    def save(self, path="drawing.png"): 
        """..."""
        cv2.imwrite(path, self._canvas)
