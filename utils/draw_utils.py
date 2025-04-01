import cv2
import numpy as np

def create_canvas(width=255, height=255, background=(0, 0, 0)):
    """Crea un nuevo lienzo con fondo personalizado."""
    canvas = np.zeros((height, width, 3), dtype="uint8")
    canvas[:] = background
    return canvas

def draw_line(canvas, start, end, color=(255, 255, 255), thickness=1):
    cv2.line(canvas, start, end, color, thickness)
    return canvas

def draw_rectangle(canvas, top_left, bottom_right, color=(255, 255, 255), thickness=1):
    cv2.rectangle(canvas, top_left, bottom_right, color, thickness)
    return canvas

def draw_circle(canvas, center, radius, color=(255, 255, 255), thickness=1):
    cv2.circle(canvas, center, radius, color, thickness)
    return canvas

def draw_polygon(canvas, points, color=(255, 255, 255), thickness=1):
    pts = np.array(points, np.int32).reshape((-1, 1, 2))
    cv2.polylines(canvas, [pts], isClosed=True, color=color, thickness=thickness)
    return canvas

def draw_text(canvas, text, position, font_scale=1, color=(255, 255, 255), thickness=2):
    cv2.putText(canvas, text, position, cv2.FONT_HERSHEY_PLAIN, font_scale, color, thickness)
    return canvas

def draw_arrow(canvas, start, end, color=(255, 255, 255), thickness=1, tip_length=0.1):
    """Dibuja una flecha (útil para visualizar flujo óptico o direcciones)."""
    cv2.arrowedLine(canvas, start, end, color, thickness, tipLength=tip_length)
    return canvas

def draw_ellipse(canvas, center, axes, angle, color=(255, 255, 255), thickness=1):
    """Dibuja una elipse con rotación personalizada."""
    cv2.ellipse(canvas, center, axes, angle, 0, 360, color, thickness)
    return canvas

def add_grid(canvas, spacing=50, color=(100, 100, 100), thickness=1):
    """Añade una cuadrícula al canvas (útil para calibrar o debuggear)."""
    h, w = canvas.shape[:2]
    for x in range(0, w, spacing):
        cv2.line(canvas, (x, 0), (x, h), color, thickness)
    for y in range(0, h, spacing):
        cv2.line(canvas, (0, y), (w, y), color, thickness)
    return canvas

def blend_with_canvas(canvas, image, alpha=0.5, x=0, y=0):
    """Superpone una imagen sobre el canvas con transparencia."""
    overlay = canvas.copy()
    h, w = image.shape[:2]
    overlay[y:y+h, x:x+w] = cv2.addWeighted(overlay[y:y+h, x:x+w], alpha, image, 1-alpha, 0)
    return overlay

def random_shapes(canvas, count=5, max_size=50):
    """Genera figuras aleatorias para testing/demos."""
    for _ in range(count):
        color = tuple(np.random.randint(0, 255, 3).tolist())
        pt1 = (np.random.randint(0, canvas.shape[1]), np.random.randint(0, canvas.shape[0]))
        pt2 = (pt1[0] + np.random.randint(10, max_size), pt1[1] + np.random.randint(10, max_size))
        cv2.rectangle(canvas, pt1, pt2, color, -1)
    return canvas
