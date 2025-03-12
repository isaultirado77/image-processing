import cv2
import numpy as np

canvas = np.zeros((300, 300, 3), dtype = "uint8")

withe = (255, 255, 255)

# Define center
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)

for r in range(0, 175, 25): 
    cv2.circle(img=canvas, center=(centerX, centerY), radius=r, color=withe)

cv2.imshow("Circles", canvas)
cv2.waitKey(0)

for i in range(0, 25): 
    rad = np.random.randint(5, high=200)
    col = np.random.randint(0, high=256, size=(3,)).tolist()

    pt = np.random.randint(0, high=300, size=(2, ))

    cv2.circle(canvas, tuple(pt), rad, col, -1)

cv2.imshow(mat=canvas, winname="Random circles")
cv2.waitKey(0)