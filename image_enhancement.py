import cv2
import numpy as np
from typing import Tuple, List, Optional, Union

def adjust_brightness(image: np.ndarray, beta: float) -> np.ndarray:
    """
    Ajusta el brillo de una imagen (suma un valor constante a todos los píxeles).
    
    Args:
        image: Imagen de entrada en formato BGR o escala de grises.
        beta: Valor de brillo a añadir (puede ser negativo para oscurecer).
              Rango recomendado: [-100, 100].
    
    Returns:
        Imagen con el brillo ajustado (mismo formato que la entrada).
    """
    return cv2.convertScaleAbs(image, alpha=1.0, beta=beta)  # https://docs.opencv.org/4.x/d2/de8/group__core__array.html#ga3460e9c9f37b563ab9dd550c4d8c4e7d

def adjust_contrast(image: np.ndarray, alpha: float) -> np.ndarray:
    """
    Ajusta el contraste de una imagen (multiplica los valores de píxel por un factor).
    
    Args:
        image: Imagen de entrada en formato BGR o escala de grises.
        alpha: Factor de contraste (1.0 = sin cambio, <1 reduce contraste, >1 aumenta).
               Rango recomendado: [0.5, 2.0].
    
    Returns:
        Imagen con el contraste ajustado.
    """
    return cv2.convertScaleAbs(image, alpha=alpha, beta=0)

def adjust_brightness_contrast(image: np.ndarray, alpha: float, beta: float) -> np.ndarray:
    """
    Ajusta simultáneamente brillo y contraste.
    
    Args:
        alpha: Factor de contraste (1.0 = sin cambio).
        beta: Valor de brillo a añadir.
    
    Returns:
        Imagen ajustada.
    """
    return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

def histogram_equalization(image: np.ndarray) -> np.ndarray:
    """
    Ecualización del histograma para mejorar el contraste en imagenes en escala de grises. 
    """
    if len(image) == 3: 
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    return cv2.equalizeHist(image) 

# https://docs.opencv.org/4.x/d5/daf/tutorial_py_histogram_equalization.html
def clahe(image: np.ndarray, 
          clip_limit: float = 2.0, 
          grid_size: Tuple[int, int] = (8, 8)) -> np.ndarray:
    """
    CLAHE: Contrast Limited Adaptative Histogram Equalizable
    Ecualización adaptativa del histograma usando CLAHE. 
    Funciona mejor que la ecualización clásica para imagenes con iluminación variada. 

     Args:
        image: Imagen en escala de grises o BGR.
        clip_limit: Límite de contraste para evitar amplificación de ruido (valores típicos: 1.0-3.0).
        grid_size: Tamaño de la cuadrícula para procesamiento local (ej: (8,8)).
    
    Returns:
        Imagen procesada con CLAHE.
    """
    if len(image) == 3: 
        # Convertir a LAB format y aplicar CLAHE en el canal L (luminicencia)
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=grid_size)
        l = clahe.apply(l)
        lab = cv2.merge((l, a, b))
        return cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
    else: 
        clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=grid_size)
        return clahe.apply(image)

def gamma_correction():
    pass

def sharpen():
    pass

def auto_contrast():
    pass