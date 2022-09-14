import numpy as np
import cv2 as cv

src = "benzema.png"
img = cv.imread(src,0)
t = 128
H,W = img.shape[:2]
img_a = np.zeros((H,W))

# membuat citra biner
for i in range(H):
    for j in range(W):
        if img[i,j] >= t:
            img_a[i,j] = 255
        elif img[i, j] < t:
            img_a[i,j] = 0

img_b = np.zeros((H,W))

# membuat komplemen dari citra biner
for i in range(H):
    for j in range(W):
        if img_a[i,j] == 0:
            img_b[i,j] = 255
        elif img_a[i, j] == 255:
            img_b[i,j] = 0
        
        
cv.imshow("img_a : biner", img_a)
cv.imshow("img_b : komplemen", img_b)
cv.waitKey(0)
cv.destroyAllWindows()