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
def sobel_edges(image: np.ndarray,
                dx: int = 1, 
                dy: int = 1, 
                ksize: int = 3, 
                normalize: bool = True) -> np.ndarray:
    """
    Detecta bordes usando operadores Sobel en direcciones X e Y.
    """
    sobelx = cv2.Sobel(image, cv2.CV_64F, dx, 0, ksize=ksize)
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, dy, ksize=ksize)
    grad = np.sqrt(sobelx**2 + sobely**2)
    
    if normalize:
        grad = cv2.normalize(grad, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    
    return grad

def canny_edges(image: np.ndarray, 
                low_threshold: float = 50, 
                upper_threshold: float = 150, 
                aperture_size: int = 3, 
                l2_gradient: bool = False) -> np.ndarray: 
    """
    Detecta bordes usando el algoritmo Canny.
    """
    return cv2.Canny(image, low_threshold, upper_threshold,
                      apertureSize=aperture_size, L2gradient=l2_gradient)

def laplacian_edges(image: np.ndarray, 
                    ksize: int = 3, 
                    normalize: bool = True) -> np.ndarray: 
    """
    Detecya bordes usando el operador laplaciano
    """
    lap = cv2.Laplacian(image, ddepth=cv2.CV_64F, ksize=ksize)

    if normalize: 
        lap = cv2.normalize(lap, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    
    return lap

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
def apply_kernel(image: np.ndarray,
                 kernel: np.ndarray, 
                 normalize: bool = True) -> np.ndarray: 
    """
    Aplica un kernel personalizado a la imagen. 
    """
    if normalize:
        kernel = kernel / np.sum(np.abs(kernel))
    
    return cv2.filter2D(image, -1, kernel)

def emboss_filter(image: np.ndarray,
                  direction: str = "top-left"): 
    """
    Aplica efecto de relieve (emboss).
    """
    kernels = {
        "top-left": np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]]),
        "top": np.array([[-1, -1, 0], [-1, 1, 1], [0, 1, 1]]),
        "top-right": np.array([[0, -1, -2], [1, 1, -1], [2, 1, 0]])
    }
    kernel = kernels.get(direction, kernels["top-left"])
    return apply_kernel(image, kernel)

### 5. Filtros Morfológicos ###
def morphological_operation(): 
    """
    """
    pass