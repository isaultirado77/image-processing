import cv2
import numpy as np
from typing import Tuple, List, Union, Optional


### 1. Filtros de Suavizado (Denoising) ###
def avgerage_blur(image: np.ndarray,
                  kernel_size: Tuple[int, int] = (5, 5)) -> np.ndarray: 
    """
    Aplica filtro de promedio.
    Args:
        image: Imagen de entrada
        kernel_size: Tamaño del kernel (ancho, alto) - deben ser impares
    """
    return cv2.blur(image, kernel_size)

def median_blur(image: np.ndarray, 
               kernel_size: int = 5) -> np.ndarray:
    """
    Aplica filtro de mediana, efectivo para ruido 'salt-and-pepper'.

    Args:
        image: Imagen de entrada
        kernel_size: Tamaño del kernel (entero impar, típico 3, 5 o 7)
    """
    return cv2.medianBlur(image, kernel_size)

def gaussian_blur(image: np.ndarray, 
                  kernel_size: Tuple[int, int] = (5, 5), 
                  sigma: float = 0) -> np.ndarray: 
    """
    Aplica filtro Gaussiano para suavizado y reducción de ruido.
    Args:
        image: Imagen de entrada
        kernel_size: Tamaño del kernel (ancho, alto) - deben ser impares
        sigma: Desviación estándar en X (0 para cálculo automático)
    """
    return cv2.GaussianBlur(image, kernel_size, sigma)

def bilateral_filter(image: np.ndarray,
                     d: int = 9, 
                     sigma_color: float = 75, 
                     sigma_space: float = 75) -> np.ndarray: 
    """
    Filtro bilateral que preserva bordes mientras reduce ruido.
    Args:
        image: Imagen de entrada
        d: Diámetro del vecindario (tamaño del filtro)
        sigma_color: Filtro en el espacio de color
        sigma_space: Filtro en el espacio geométrico
    """
    return cv2.bilateralFilter(image, d, sigma_color, sigma_space)

### 2. Filtros de Detección de Bordes ###
def sobel_edges(): 
    """
    Detecta bordes usando operadores Sobel en direcciones X e Y.
    """
    pass

def canny_edges(): 
    """
    """
    pass
def laplacian_edges(): 
    """
    """
    pass

### 3. Filtros de Enfoque (Sharpening) ###
def sharpen(): 
    """
    """
    pass

def unsharp_mask(): 
    """
    """
    pass

### 4. Filtros Personalizados ###
def apply_kernel(): 
    """
    """
    pass

def emboss_filter(): 
    """
    """
    pass

### 5. Filtros Morfológicos ###
def morphological_operation(): 
    """
    """
    pass