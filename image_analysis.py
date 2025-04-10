import cv2
import numpy as np

### 1. Detección de Contornos y Formas ###
def find_contours():
    """
    """
    pass

def approximate_contour():
    """
    """
    pass

def detect_shapes(): 
    """
    """
    pass


### 2. Segmentación ###
def simple_threshold(image: np.ndarray,
                     threshold_value: int = 127,
                     max_value: int = 255,
                     method: str = "binary") -> tuple[float, np.ndarray]:
    """
    Aplica umbralización a una imagen en escala de grises.

    Params: 
    - image (np.ndarray): Imagen de entrada, debe ser en escala de grises.
    - threshold_value (int): Valor de umbral.
    - max_value (int): Valor máximo a asignar cuando se cumpla la condición.
    - method (str): Tipo de umbral. Uno de: "binary", "binary_inv", "trunc", "tozero", "tozero_inv".

    Returns:
    - T (float): El valor del umbral usado.
    - thresh (np.ndarray): Imagen de salida umbralizada.
    """
    if len(image.shape) != 2:
        raise ValueError("La imagen debe estar en escala de grises (1 canal).")

    methods = {
        "binary": cv2.THRESH_BINARY,
        "binary_inv": cv2.THRESH_BINARY_INV,
        "trunc": cv2.THRESH_TRUNC,
        "tozero": cv2.THRESH_TOZERO,
        "tozero_inv": cv2.THRESH_TOZERO_INV
    }

    if method not in methods:
        raise ValueError(f"Método de umbralización '{method}' no válido. "
                         f"Opciones disponibles: {list(methods.keys())}")

    T, thresh = cv2.threshold(image, threshold_value, max_value, methods[method])
    return T, thresh


def adaptive_threshold(image: np.ndarray, 
                       max_value: int = 255, 
                       method: str = "gaussian", 
                       threshold_type: str = "binary",
                       block_size: int = 11, 
                       C: int = 2) -> np.ndarray:
    """
    Aplica umbralización adaptativa para imágenes con iluminación no uniforme.

    Params:
    - image (np.ndarray): Imagen de entrada en escala de grises.
    - max_value (int): Valor que se asigna si la condición se cumple (normalmente 255).
    - method (str): Método de cálculo del umbral local ('mean' o 'gaussian').
    - threshold_type (str): Tipo de umbral ('binary' o 'binary_inv').
    - block_size (int): Tamaño del área vecina usada para calcular el umbral. Debe ser impar y > 1.
    - C (int): Valor constante que se resta del umbral calculado.

    Returns:
    - np.ndarray: Imagen binarizada por umbral adaptativo.
    """
    if len(image.shape) != 2:
        raise ValueError("La imagen debe estar en escala de grises (1 canal).")

    method_map = {
        "mean": cv2.ADAPTIVE_THRESH_MEAN_C,
        "gaussian": cv2.ADAPTIVE_THRESH_GAUSSIAN_C
    }
    thresh_type_map = {
        "binary": cv2.THRESH_BINARY,
        "binary_inv": cv2.THRESH_BINARY_INV
    }

    if method not in method_map:
        raise ValueError(f"Método '{method}' no válido. Opciones: {list(method_map.keys())}")
    if threshold_type not in thresh_type_map:
        raise ValueError(f"Tipo de umbral '{threshold_type}' no válido. Opciones: {list(thresh_type_map.keys())}")
    if block_size % 2 == 0 or block_size <= 1:
        raise ValueError("El block_size debe ser un número impar mayor que 1.")

    return cv2.adaptiveThreshold(
        src=image,
        maxValue=max_value,
        adaptiveMethod=method_map[method],
        thresholdType=thresh_type_map[threshold_type],
        blockSize=block_size,
        C=C
    )

def otsu_threshold(image: np.ndarray,
                   max_value: int = 255,
                   threshold_type: str = "binary") -> tuple[float, np.ndarray]:
    """
    Aplica Otsu's Thresholding a una imagen en escala de grises.

    Params:
        image: Imagen de entrada (debe estar en escala de grises).
        max_value: Valor asignado a los píxeles que cumplen la condición.
        threshold_type: Tipo de umbralización ('binary' o 'binary_inv').

    Returns:
        T: Valor del umbral calculado automáticamente por Otsu.
        thresh: Imagen umbralizada resultante.
    """
    threshold_map = {
        "binary": cv2.THRESH_BINARY,
        "binary_inv": cv2.THRESH_BINARY_INV
    }

    if threshold_type not in threshold_map:
        raise ValueError(f"threshold_type '{threshold_type}' no válido.")

    # Usamos bitwise OR para combinar el tipo de umbral con OTSU
    thresh_type_flag = threshold_map[threshold_type] | cv2.THRESH_OTSU
    T, thresh = cv2.threshold(src=image,
                              thresh=0,
                              maxval=max_value,
                              type=thresh_type_flag)
    return T, thresh

def traingle_threshold(): 
    pass

def watershed_segmentation():
    """
    Segmentación basada en watershed.
    """
    print()
    pass


### 3. Análisis de Características ###
def compute_moments(): 
    """
    """
    pass

def compute_shape_descriptors():
    """
    """
    pass

### 4. Detección de Bordes y Esquinas ###
def detect_edges(): 
    """
    """
    pass

def detect_corners(): 
    """
    """
    pass

### 5. Visualización ###
def draw_contours(): 
    """
    """
    pass

def draw_corners(): 
    """
    """
    pass