import cv2
import numpy as np
import matplotlib.pyplot as plt
from typing import Union, List, Tuple, Optional

### 1. Cálculo de Histogramas ###
def compute_histogram(image: np.ndarray, 
                     mask: Optional[np.ndarray] = None, 
                     bins: int = 256, 
                     range: Tuple[float, float] = (0, 256)) -> np.ndarray:
    """
    Calcula el histograma de una imagen (escala de grises o color).
    """
    if len(image.shape) == 3:  # Imagen color
        channels = cv2.split(image)
        histograms = []
        for i, ch in enumerate(channels):
            hist = cv2.calcHist([ch], [0], mask, [bins], range)
            histograms.append(hist)
        return histograms
    else:  # Escala de grises
        return cv2.calcHist([image], [0], mask, [bins], range)

def compute_cumulative_histogram(hist: np.ndarray) -> np.ndarray:
    """
    Calcula el histograma acumulativo.
    """
    cum_hist = hist.cumsum()
    return cum_hist / cum_hist[-1]  # Normalización

### 2. Visualización ###
def plot_histogram(hist: Union[np.ndarray, List[np.ndarray]], 
                  title: str = "Histograma", 
                  colors: Tuple[str] = ('b', 'g', 'r'), 
                  cumulative: bool = False,
                  ax: Optional[plt.Axes] = None) -> None:
    """
    Visualiza uno o más histogramas usando Matplotlib.
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 5))
    
    if isinstance(hist, list):  # Múltiples canales
        for h, color in zip(hist, colors):
            h = h.flatten()
            if cumulative:
                h = compute_cumulative_histogram(h)
            ax.plot(h, color=color)
    else:  # Un solo canal
        h = hist.flatten()
        if cumulative:
            h = compute_cumulative_histogram(h)
        ax.plot(h, color='gray')
    
    ax.set_title(title)
    ax.set_xlim([0, 256])
    ax.grid(True, linestyle='--', alpha=0.7)

def plot_histogram_3d(image: np.ndarray, 
                     bins: int = 256,
                     title: str = "Histograma 3D de Color") -> None:
    """
    Visualiza histograma 3D para imágenes color (BGR).
    """
    from mpl_toolkits.mplot3d import Axes3D
    
    # Preparar datos
    pixels = image.reshape((-1, 3))
    b, g, r = pixels[:, 0], pixels[:, 1], pixels[:, 2]
    
    # Crear figura 3D
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Scatter plot 
    ax.scatter(b, g, r, c=pixels/255.0, marker='.', s=1, alpha=0.1)
    
    # Configuración
    ax.set_xlabel('Canal Azul')
    ax.set_ylabel('Canal Verde')
    ax.set_zlabel('Canal Rojo')
    ax.set_title(title)
    plt.tight_layout()

### 3. Operaciones con Histogramas ###
def normalize_histogram(hist: np.ndarray) -> np.ndarray:
    """
    Normaliza un histograma a [0, 1].
    """
    return hist / hist.sum()

def compare_histograms(hist1: np.ndarray, 
                      hist2: np.ndarray, 
                      method: str = 'correlation') -> float:
    """
    Compara dos histogramas usando métricas de OpenCV.
    """
    methods = {
        'correlation': cv2.HISTCMP_CORREL,
        'chisqr': cv2.HISTCMP_CHISQR,
        'intersect': cv2.HISTCMP_INTERSECT,
        'bhattacharyya': cv2.HISTCMP_BHATTACHARYYA
    }
    return cv2.compareHist(hist1, hist2, methods[method.lower()])

def histogram_matching(source: np.ndarray, 
                      reference: np.ndarray) -> np.ndarray:
    """
    Ajusta el histograma de una imagen para que coincida con una referencia.
    """
    # Calcular histogramas acumulativos
    src_hist = compute_cumulative_histogram(compute_histogram(source))
    ref_hist = compute_cumulative_histogram(compute_histogram(reference))
    
    # Mapeo de intensidades
    lut = np.interp(src_hist.flatten(), ref_hist.flatten(), np.arange(256))
    
    # Aplicar LUT
    return cv2.LUT(source, lut.astype('uint8'))

### 4. Herramientas Avanzadas ###
def get_histogram_stats(hist: np.ndarray) -> dict:
    """
    Calcula estadísticas descriptivas de un histograma.
    """
    bins = np.arange(256)
    mean = np.sum(bins * hist.flatten())
    variance = np.sum((bins - mean)**2 * hist.flatten())
    
    return {
        'mean': mean,
        'median': np.argmax(np.cumsum(hist) >= 0.5),
        'std': np.sqrt(variance),
        'entropy': -np.sum(hist * np.log2(hist + 1e-10))  # Evitar log(0)
    }

def plot_histogram_comparison(image1: np.ndarray, 
                             image2: np.ndarray, 
                             titles: Tuple[str] = ('Imagen 1', 'Imagen 2')) -> None:
    """
    Compara visualmente histogramas de dos imágenes con subplots.
    """
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # Imágenes
    axes[0, 0].imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
    axes[0, 0].set_title(titles[0])
    axes[0, 0].axis('off')
    
    axes[0, 1].imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
    axes[0, 1].set_title(titles[1])
    axes[0, 1].axis('off')
    
    # Histogramas
    if len(image1.shape) == 3:
        hist1 = compute_histogram(image1)
        plot_histogram(hist1, ax=axes[1, 0], cumulative=False)
    else:
        hist1 = compute_histogram(image1)
        plot_histogram(hist1, ax=axes[1, 0], colors=('gray',), cumulative=False)
    
    if len(image2.shape) == 3:
        hist2 = compute_histogram(image2)
        plot_histogram(hist2, ax=axes[1, 1], cumulative=False)
    else:
        hist2 = compute_histogram(image2)
        plot_histogram(hist2, ax=axes[1, 1], colors=('gray',), cumulative=False)
    
    plt.tight_layout()

