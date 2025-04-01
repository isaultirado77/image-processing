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

def show_image(canvas, name="Drawing"):
    cv2.imshow(name, canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def save_image(canvas, path="drawing.png"):
    cv2.imwrite(path, canvas)
