import cv2
import numpy as np
from typing import Union, Optional, Tuple, List


def translate(image: np.ndarray, x: float, y: float) -> np.ndarray:
    """Desplaza una imagen en las direcciones x e y."""
    M = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

def rotate(image: np.ndarray,
           angle: float,
           center: Tuple[int, int] = (152, 152),
           scale: float = 1.0) -> np.ndarray:
    """Rota una imagen alrededor de un centro con un ángulo y escala especificados."""
    h, w = image.shape[:2]
    center = center or (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    return cv2.warpAffine(image, M, (w, h))

def resize(image: np.ndarray, width: int = 256, height: int = 256,
           inter: int = cv2.INTER_AREA):
    """Redimensiona una imagen manteniendo la relación de aspecto."""
    h, w = image.shape[:2]
    
    if width is None and height is None:
        return image.copy()
    
    dim = (width, int(h * (width/w))) if width else (int(w * (height/h)), height)
    return cv2.resize(image, dim, interpolation=inter)

def crop(image: np.ndarray, x_start: int, y_start: int,
         x_end: int, y_end: int) -> np.ndarray:
    return image[y_start:y_end, x_start:x_end]

def convert_color(image: np.ndarray, color_space: str = "GRAY") -> np.ndarray:
    conversions = {
        "GRAY": cv2.COLOR_BGR2GRAY,
        "HSV": cv2.COLOR_BGR2HSV,
        "LAB": cv2.COLOR_BGR2LAB,
        "RGB": cv2.COLOR_BGR2RGB
    }
    if color_space not in conversions:
        raise ValueError(f"Color space must be one of {list(conversions.keys())}")
    
    return cv2.cvtColor(image, conversions[color_space])

def add(image1: np.ndarray, image2: np.ndarray) -> np.ndarray:
    """Suma dos imágenes pixel por pixel."""
    return cv2.add(image1, image2)

def subtract(image1: np.ndarray, image2: np.ndarray) -> np.ndarray:
    """Resta dos imágenes pixel por pixel."""
    return cv2.subtract(image1, image2)

def multiply(image1: np.ndarray, image2: np.ndarray) -> np.ndarray:
    """Multiplica dos imágenes pixel por pixel."""
    return cv2.multiply(image1, image2)

def apply_mask(image: np.ndarray, mask: np.ndarray) -> np.ndarray:
    """Aplica una máscara binaria a una imagen."""
    return cv2.bitwise_and(image, image, mask=mask)