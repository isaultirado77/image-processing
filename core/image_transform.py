import cv2
import numpy as np

def translate(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

def rotate(image, angle, center=None, scale=1.0):
    h, w = image.shape[:2]
    center = center or (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    return cv2.warpAffine(image, M, (w, h))

def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    h, w = image.shape[:2]
    
    if width is None and height is None:
        return image.copy()
    
    dim = (width, int(h * (width/w))) if width else (int(w * (height/h)), height)
    return cv2.resize(image, dim, interpolation=inter)

def crop(image, x_start, y_start, x_end, y_end):
    return image[y_start:y_end, x_start:x_end]

def convert_color(image, color_space="GRAY"):
    conversions = {
        "GRAY": cv2.COLOR_BGR2GRAY,
        "HSV": cv2.COLOR_BGR2HSV,
        "LAB": cv2.COLOR_BGR2LAB,
        "RGB": cv2.COLOR_BGR2RGB
    }
    
    if color_space not in conversions:
        raise ValueError(f"Color space must be one of {list(conversions.keys())}")
    
    return cv2.cvtColor(image, conversions[color_space])

add = cv2.add
subtract = cv2.subtract
multiply = cv2.multiply
apply_mask = lambda image, mask: cv2.bitwise_and(image, image, mask=mask)