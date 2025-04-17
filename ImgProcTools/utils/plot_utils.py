from typing import List, Tuple
import matplotlib.pyplot as plt
import cv2


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