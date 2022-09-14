import numpy as np
import cv2 as cv
from PIL import Image
from math import sin, cos


def rotasi(derajat):
    src = "benzema.png"
    img = cv.imread(src,0)

    W,H = img.shape[:2]

    new_img = np.zeros((W,H), np.uint8)

    x_mid = W // 2
    y_mid = H // 2

    for x in range(W):
        for y in range(H):
            
            theta = derajat * 22/7 / 180

            x_baru = (cos(theta) * (x - x_mid) - sin(theta)
                      * (y - y_mid) + x_mid)
            y_baru = (sin(theta) * (x - x_mid) + cos(theta)
                      * (y - y_mid) + y_mid)

            if (x_baru >= W or y_baru >= H
                    or x_baru < 0 or y_baru < 0):
                new_img[x, y] = 0
            else:
                new_img[x, y] = img[int(x_baru), int(y_baru)]

    new_img = np.reshape(new_img, (W, H))
    cv.imshow("original", img)
    cv.imshow("rotasi", new_img)
    cv.waitKey(0)
    cv.destroyAllWindows()

rotasi(45)
rotasi(180)