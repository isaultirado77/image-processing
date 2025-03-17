import numpy as np
import cv2

class ImageTransform: 
    def __init__(self, image):
        self._image = image

    def translation(self, x, y): 
        M = np.float32([[1, 0, x], [0, 1, y]])
        shifted = cv2.warpAffine(self._image, M, (self._image.shape[1], self._image.shape[0]))
        return shifted

    def rotation(self, angle: float, center: tuple = None, scale=1.0): 
        (h, w) = self._image[:2]

        if center is None:
            center = (w // 2, h // 2)
        
        M = cv2.getRotationMatrix2D(center, angle, scale)
        rotated = cv2.warpAffine(self._image, M, (w, h))
        return rotated

    def resizing(self, width: int = None, height: int = None, inter=cv2.INTER_AREA): 
        (h, w) = self._image[:2]
        if width is None and height is None: 
            return self._image
        
        if width is None: 
            r = height / float(h)
            dim = (int(w * r), height)
        else: 
            r = width / float(w)
            dim = (width, int(h * r))
        
        resized = cv2.resize(self._image, dim, interpolation=inter)
        return resized
    
    def cropp(self, x_start: int, y_start: int, x_end: int, y_end: int): 
        """Recorta la imagen dentro de las coordenadas especificadas."""
        cropped = self._image[y_start:y_end, x_start:x_end]
        return cropped
    
    def add(self, other): 
        return cv2.add(self._image, other)

    def substract(self, other): 
        return cv2.subtract(self._image, other)

    def multiply(self, other): 
        return cv2.multiply(self._image, other)

    def apply_mask(self, mask): 
        return cv2.bitwise_and(self._image, self._image, mask=mask)

    def split_channles(self): 
        return cv2.split(self._image)

    def merge_channels(self, channles: list):
        return cv2.merge(channles)
    
    def convert_color_space(self, color_space : str = "GRAY"): 
        """Convierte la imagen a un espacio de color especificado."""
        color_spaces = {
            "GRAY": cv2.COLOR_BGR2GRAY,
            "HSV": cv2.COLOR_BGR2HSV,
            "LAB": cv2.COLOR_BGR2LAB,
            "RGB": cv2.COLOR_BGR2RGB
        }

        if color_space not in color_space: 
            raise ValueError(f"Color space not supported. Choose from {color_spaces.values}.")
        
        return cv2.cvtColor(self._image, color_spaces[color_space])
    