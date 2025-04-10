import numpy as np
import cv2
from typing import Tuple, Union, Optional
from utils.draw_utils import draw_circle

def compute_fft(image: np.ndarray) -> np.ndarray:
    """
    Calcula la Transformada de Fourier de una imagen en escala de grises.
    """
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fft = np.fft.fft2(image)
    fft_shifted = np.fft.fftshift(fft)  # fft2 coloca las frecuencias bajas en las esquinas y las altas en el centro
    return fft_shifted 

def inverse_fft(fft: np.ndarray) -> np.ndarray: 
    """
    Reconstruye una imagem a partir de su FFT desplazada. 
    """
    fft_unshifted = np.fft.ifftshift(fft)   # Deshacer el shift
    img_reconstructed = np.fft.ifft2(fft_unshifted)  # Aplicar la TF inversa
    img_reconstructed = np.real(img_reconstructed)  # Tomar solo la parte real
    return img_reconstructed.astype(np.float32)

def apply_fft_filter(image: np.ndarray, mask: np.ndarray) -> np.ndarray:
    """
    Aplica un foltro en el dominio de las frecuencias usando una máscara. 
    """
    if len(image) == 3:  # Aplica filtrado en cada canal
        channels = cv2.split(image)
        filtered_channels = []
        for ch in channels: 
            fft = compute_fft(ch)
            filtered = fft * mask
            im_back = inverse_fft(filtered)
            filtered_channels.append(im_back)
            return cv2.merge(filtered_channels)  # test para ordenar los channels correctamente
    else: 
        fft = compute_fft(image)
        filtered = fft * mask
        im_back = inverse_fft(filtered)
        return im_back  # tested: working

def create_ideal_filter(shape: Tuple[int, int], 
                        radius: int,
                        high_pass: bool = False) -> np.ndarray:
    """
    Crea un filtro ideal (pasa-bajas o pasa-altas).
    """
    rows, cols = shape
    center = (rows // 2, cols // 2)
    mask = np.zeros(shape=(rows, cols), dtype=np.uint8)
    cv2.circle(img=mask, center=center, radius=radius, color=1, thickness=-1)
    # mask = draw_circle(mask, center, radius, color=1, thickness=-1)  # test 
    return 1 - mask if high_pass else mask

def create_butterworth_filter(shape: Tuple[int, int],
                              radius: int, 
                              order: int = 2, 
                              high_pass: bool = False) -> np.ndarray:
    """
    Crea un filtro Butterworth (para suavizaso en bordes). 
    """
    rows, cols = shape
    crow, ccol = rows // 2, cols // 2  # centros del mask
    x = np.arange(cols) - ccol
    y = np.arange(rows) -crow
    xx, yy = np.meshgrid(x, y)  # Grid con centro en el centro de la imagen
    d = np.sqrt(xx**2 + y**2)  # distancia radial desde cada punto al centro (frecuencia cero)
    mask = 1 / (1 + (d/radius)**(2*order))  # filtro final usando 1 / sqrt(1 - w^(2n))
    return 1 - mask if high_pass else mask

def create_gaussian_filter(shape: Tuple[int, int],
                           sigma: float, 
                           high_pass: bool = False) -> np.ndarray:
    """Crea un filtro gaussiano. """
    rows, cols = shape
    crow, ccol = rows // 2, cols // 2  # centros del mask
    x = np.arange(cols) - ccol
    y = np.arange(rows) -crow
    xx, yy = np.meshgrid(x, y)  # Grid con centro en el centro de la imagen
    d = np.sqrt(xx**2 + y**2)  # distancia radial desde cada punto al centro (frecuencia cero)
    mask = np.exp(-(d**2)/(2*(sigma**2)))
    return 1 - mask if high_pass else mask