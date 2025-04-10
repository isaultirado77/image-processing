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

def apply_fft_filter():
    pass

def create_ideal_filter():
    pass

def create_butterworth_filter():
    pass

def create_gaussian_filter(): 
    pass