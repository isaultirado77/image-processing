import cv2
import numpy as np
from typing import List, Tuple


def create_canvas(width: int = 255, 
                height: int = 255, 
                background: Tuple[int, int, int] = (0, 0, 0)) -> np.ndarray:
    """Crea un nuevo lienzo con fondo personalizado."""
    canvas = np.zeros((height, width, 3), dtype="uint8")
    canvas[:] = background
    return canvas

def draw_line(canvas: np.ndarray, 
              start: Tuple[int, int], 
              end: Tuple[int, int], 
              color: Tuple[int, int, int] = (255, 255, 255), 
              thickness: int = 1) -> np.ndarray:
    cv2.line(canvas, start, end, color, thickness)
    return canvas

def draw_rectangle(canvas: np.ndarray,
                   top_left: Tuple[int, int],
                   bottom_right: Tuple[int, int],
                   color: Tuple[int, int, int] = (255, 255, 255),
                   thickness: int = 1) -> np.ndarray:
    cv2.rectangle(canvas, top_left, bottom_right, color, thickness)
    return canvas

def draw_circle(canvas: np.ndarray,
                center: Tuple[int, int],
                radius: int,
                color: Tuple[int, int, int] = (255, 255, 255), 
                thickness: int = 1) -> np.ndarray:
    cv2.circle(canvas, center, radius, color, thickness)
    return canvas

def draw_polygon(canvas: np.ndarray,
                points: List[Tuple[int, int]], 
                color: Tuple[int, int, int] = (255, 255, 255),
                thickness: int = 1) -> np.ndarray:
    pts = np.array(points, np.int32).reshape((-1, 1, 2))
    cv2.polylines(canvas, [pts], isClosed=True, color=color, thickness=thickness)
    return canvas

def draw_text(canvas: np.ndarray,
              text: str, position: Tuple[int, int],
              font_scale: float = 1,
              color: Tuple[int, int, int] = (255, 255, 255),
              thickness: int = 2) -> np.ndarray:
    cv2.putText(canvas, text, position, cv2.FONT_HERSHEY_PLAIN, font_scale, color, thickness)
    return canvas

def draw_arrow(canvas: np.ndarray,
               start: Tuple[int, int],
               end: Tuple[int, int],
               color: Tuple[int, int, int] = (255, 255, 255),
               thickness: int = 1,
               tip_length: float = 0.1) -> np.ndarray:
    """Dibuja una flecha (útil para visualizar flujo óptico o direcciones)."""
    cv2.arrowedLine(canvas, start, end, color, thickness, tipLength=tip_length)
    return canvas

def draw_ellipse(canvas: np.ndarray,
                 center: Tuple[int, int],
                 axes: Tuple[int, int],
                 angle: float,
                 color: Tuple[int, int, int] = (255, 255, 255),
                 thickness: int = 1) -> np.ndarray:
    """Dibuja una elipse con rotación personalizada."""
    cv2.ellipse(canvas, center, axes, angle, 0, 360, color, thickness)
    return canvas

def add_grid(canvas: np.ndarray,
             spacing: int = 50,
             color: Tuple[int, int, int] = (100, 100, 100),
             thickness: int = 1) -> np.ndarray:
    """Añade una cuadrícula al canvas (útil para calibrar o debuggear)."""
    h, w = canvas.shape[:2]
    for x in range(0, w, spacing):
        cv2.line(canvas, (x, 0), (x, h), color, thickness)
    for y in range(0, h, spacing):
        cv2.line(canvas, (0, y), (w, y), color, thickness)
    return canvas

def blend_with_canvas(canvas: np.ndarray,
                      image: np.ndarray,
                      alpha: float = 0.5,
                      x: int = 0, 
                      y: int = 0) -> np.ndarray:
    """Superpone una imagen sobre el canvas con transparencia."""
    overlay = canvas.copy()
    h, w = image.shape[:2]
    overlay[y:y+h, x:x+w] = cv2.addWeighted(overlay[y:y+h, x:x+w], alpha, image, 1-alpha, 0)
    return overlay

def random_shapes(canvas: np.ndarray,
                  count: int = 5,
                  max_size: int = 50) -> np.ndarray:
    """Genera figuras aleatorias para testing/demos."""
    for _ in range(count):
        color = tuple(np.random.randint(0, 255, 3).tolist())
        pt1 = (np.random.randint(0, canvas.shape[1]), np.random.randint(0, canvas.shape[0]))
        pt2 = (pt1[0] + np.random.randint(10, max_size), pt1[1] + np.random.randint(10, max_size))
        cv2.rectangle(canvas, pt1, pt2, color, -1)
    return canvas

