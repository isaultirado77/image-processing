from typing import List, Tuple
import matplotlib.pyplot as plt
import cv2
import numpy as np

def side_by_side(images: List[np.ndarray], 
                titles: List[str] = None,
                figsize: Tuple[int, int] = (15, 7)) -> None:
    """Muestra múltiples imágenes en una sola figura."""
    plt.figure(figsize=figsize)
    for i, img in enumerate(images):
        plt.subplot(1, len(images), i+1)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) if len(img.shape) == 3 else plt.imshow(img, cmap='gray')
        plt.title(titles[i] if titles else f"Imagen {i+1}")
        plt.axis('off')
    plt.tight_layout()

def show_image(image: np.ndarray, 
                title: str = None) -> None:
    """Muestra una imagen (BGR o escala de grises) proveniente de OpenCV usando matplotlib.

    Args:
        image (np.ndarray): Imagen en formato numpy array. Puede ser en escala de grises (2D)
                            o en color (3 canales en formato BGR).
    """
    if image.ndim == 3:
        # Convertir de BGR a RGB antes de mostrar
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        plt.imshow(image_rgb)
    else:
        # Imagen en escala de grises
        plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()
