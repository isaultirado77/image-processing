import cv2
import numpy as np
from typing import List, Tuple

### 1. Detección de Contornos y Formas ###
def find_contours(image: np.ndarray,
                  mode: str = "external",
                  method: str = "simple") -> List[np.ndarray]:
    """
    Encuentra los contornos de una imagen binaria.
    
    Args:
    - image: Imagen binaria (np.uint8, valores 0 o 255).
    - mode: Modo de recuperación de contornos ("external", "list", "tree", "ccomp").
    - method: Método de aproximación del contorno ("none", "simple", "tc89_l1", "tc89_kcos").
    
    Returns:
    - Lista de contornos encontrados.
    """
    mode_map = {
        "external": cv2.RETR_EXTERNAL,
        "list": cv2.RETR_LIST,
        "tree": cv2.RETR_TREE,
        "ccomp": cv2.RETR_CCOMP
    }

    method_map = {
        "none": cv2.CHAIN_APPROX_NONE,
        "simple": cv2.CHAIN_APPROX_SIMPLE,
        "tc89_l1": cv2.CHAIN_APPROX_TC89_L1,
        "tc89_kcos": cv2.CHAIN_APPROX_TC89_KCOS
    }

    if mode not in mode_map:
        raise ValueError(f"Modo inválido: {mode}")
    if method not in method_map:
        raise ValueError(f"Método inválido: {method}")

    contours, _ = cv2.findContours(image, mode_map[mode], method_map[method])
    return contours


def approximate_contour(contour: np.ndarray, 
                        epsilon: float = 0.12, 
                        closed: bool = True) -> np.ndarray:
    """
    Aproxima un contorno a una forma más simple con menos puntos. 
    
    Args:
    - contour: Contorno origial (obtenido usando find_contours). 
    - epsilon: Factor de presición para la aproximación. Se multiplica por el perímetro del contorno.
               Un valor mayor genera una aproximación más agresiva (menos puntos). 
    - closed: Indica si el contorno se considera cerrado. 
    
    Returns:
    - Contorno aproximado, reprecentado por un número reducido de vértices. 
    """
    perimeter = cv2.arcLength(contour, closed)  # Calcula la longitud del perímetro de un contorno
    approx = cv2.approxPolyDP(contour, epsilon * perimeter, closed)  # Aploca el algoritmo de Dpugñas-Peucker para simplificar el contorno
    return approx

def detect_shapes(image: np.ndarray, 
                  min_area: float = 100) -> List[Tuple[str, np.ndarray]]: 
    """
    Detecta formas geométricas básicas en una imagen binaria. 

    Args:
        image: Imagen binaria de entrada
        min_area: Área mínima para considerar una forma
    
    Returns:
        Lista de tuplas (nombre_forma, contorno)
    """
    contours = find_contours(image)
    shapes = []

    for cnt in contours: 
        area = cv2.contourArea(cnt)
        if area < min_area: 
            continue

        approx = approximate_contour(cnt)
        vertices = len(approx)

        if vertices == 3:
            shape = "triangle"
        elif vertices == 4:
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = w / float(h)
            shape = "square" if 0.95 <= aspect_ratio <= 1.05 else "rectangle"
        elif vertices == 5:
            shape = "pentagon"
        elif vertices >= 6:
            shape = "circle"
        else:
            shape = "unknown"
        
        shapes.append((shape, cnt))

    return shapes

### 2. Segmentación ###
def simple_threshold(image: np.ndarray,
                     threshold_value: int = 127,
                     max_value: int = 255,
                     method: str = "binary") -> tuple[float, np.ndarray]:
    """
    Aplica umbralización a una imagen en escala de grises.

    Args: 
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

    Args:
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

    Args:
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
    pass


### 3. Análisis de Características ###  
# Dosc:
# https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html
# https://vincmazet.github.io/bip/mm/measure.html#:~:text=Solidity%20is%20the%20ratio%20of,the%20compactness%20of%20the%20object.
def compute_moments(contour: np.ndarray) -> dict: 
    """
    Calcula los momentos de un contorno y el centro geométrico (centroide) del contorno. 

    Returns: 
        Diccionario con momentos (m00, m01, ...) y centroide
    """
    M = cv2.moments(contour)
    if M['m00'] != 0: 
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
    else: 
        cx, cy = 0, 0
        return {"moments": M, "centroid": (cx, cy)}


def compute_shape_descriptors(contour: np.ndarray) -> dict:
    """
    Calcula descriptores de forma para un contorno. 
    """
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)  # Asumimos que el contorno es cerrado

    # Circularlity/Roundness  https://en.wikipedia.org/wiki/Roundness
    circularity = 0
    if perimeter > 0: 
        circularity = (4 * np.pi * area) / (perimeter ** 2)
    
    # Aspect ratio https://en.wikipedia.org/wiki/Aspect_ratio_(image)
    _, _, w, h = cv2.boundingRect(contour)
    aspect_ratio = float(w) / h if h != 0 else 0
    
    # Solidity  
    hull = cv2.convexHull(contour)  # Convex hull (optimization): Smallest convex polygon that encloses all the points. 
    # Convex hull in image processing: Is a technique for outlining the shape of an object region. 
    hull_area = cv2.contourArea(hull)  
    solidity = float(area) / hull_area if hull_area != 0 else 0

    return {
        "area": area,
        "perimeter": perimeter,
        "circularity": circularity,
        "aspect_ratio": aspect_ratio,
        "solidity": solidity
    }

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
def draw_contours(image: np.ndarray,
                  conturs: List[np.ndarray], 
                  color: Tuple[int, int, int] = (0, 255, 0), 
                  thickness: int = 2) -> np.ndarray: 
    """
    Dibuja TODOS los contornos en una copia de la imagen. 
    
    Args:
        image: Imagen de entrada
        contours: Lista de contornos
        color: Color BGR para los contornos
        thickness: Grosor de línea
    
    Returns:
        Imagen con contornos dibujados
    """
    canvas = image.copy()
    cv2.drawContours(canvas, conturs, -1, color, thickness)
    return canvas

def draw_corners(): 
    """
    """
    pass