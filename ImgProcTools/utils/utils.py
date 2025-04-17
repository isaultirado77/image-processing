import cv2
import numpy as np

def print_image_info(image: np.ndarray) -> None:
    """Imprime metadata básica de una imagen."""
    print(f"Dimensiones: {image.shape}")
    print(f"Tipo de dato: {image.dtype}")
    print(f"Rango de valores: [{image.min()}, {image.max()}]")

def scale_image(image: np.ndarray, 
               factor: float, 
               interpolation: int = cv2.INTER_LINEAR) -> np.ndarray:
    """Escala una imagen por un factor (no por dimensiones absolutas)."""
    return cv2.resize(image, None, fx=factor, fy=factor, interpolation=interpolation)