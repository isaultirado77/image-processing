import numpy as np
import cv2
from utils import draw_utils

drawer = draw_utils.Drawer(width=300, height=300)

drawer.rectangle(top_left=(25, 25), bottom_right=(275, 275), thickness=-1)
rectangle_img = drawer.canvas.copy()
drawer.show(name="Rectangle")

drawer.reset_canvas()
drawer.circle(center=(150, 150), radius=150, thickness=-1)
circle_img = drawer.canvas.copy() 
drawer.show(name="Circle")

bitwiseAnd = cv2.bitwise_and(rectangle_img, circle_img)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

bitwiseOr = cv2.bitwise_or(rectangle_img, circle_img)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

bitwiseXor = cv2.bitwise_xor(rectangle_img, circle_img)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

bitwiseNot = cv2.bitwise_not(circle_img)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)
