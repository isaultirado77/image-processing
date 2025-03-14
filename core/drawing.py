import cv2
import numpy as np

class Drawer: 
    def __init__(self, width=255, height=255, background=(0, 0, 0)):
        """
        Inicializa un lienzo en blanco o permite cargar una imagen.
        :param width: Ancho del lienzo
        :param height: Alto del lienzo
        :param background: Color de fondo en formato (B, G, R)
        """
        self.width = width
        self.height = height
        self.background_color = background
        self.reset_canvas()

    def reset_canvas(self): 
        """Reinicia el lienzo al estado inicial."""
        self.canvas = np.zeros((self.height, self.width, 3), dtype="uint8")
        self.canvas[:] = self.background_color

    def line(self, start, end, color=(255, 255, 255), thickness=1):
        cv2.line(self.canvas, start, end, color, thickness)
        return self

    def rectangle(self, top_left, bottom_right, color=(255, 255, 255), thickness=1): 
        cv2.rectangle(self.canvas, top_left, bottom_right, color, thickness)
        return self

    def circle(self, center, radius, color=(255, 255, 255), thickness=1):
        cv2.circle(self.canvas, center, radius, color, thickness)
        return self

    def polygon(self, points, color=(255, 255, 255), thickness=1): 
        pts = np.array(points, np.int32).reshape((-1, 1, 2))
        cv2.polylines(self.canvas, [pts], isClosed=True, color=color, thickness=thickness)
        return self

    def text(self, text, position, font_scale=1, color=(255, 255, 255), thickness=2): 
        cv2.putText(self.canvas, text, position, cv2.FONT_HERSHEY_PLAIN, font_scale, color, thickness)
        return self

    def show(self, name="Drawing"): 
        cv2.imshow(name, self.canvas)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return self

    def save(self, path="drawing.png"): 
        cv2.imwrite(path, self.canvas)
        return self
    
    def asarray(self): 
        return self.canvas
