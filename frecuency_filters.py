import numpy as np
import cv2
from typing import Tuple, Union, Optional


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

def create_ideal_filter():
    pass

def create_butterworth_filter():
    pass

def create_gaussian_filter(): 
    pass