import numpy as np
import cv2 as cv
from PIL import Image

def flipping_vertikal(img):
    W,H = img.shape[:2]

    new_img = np.zeros((W,H), np.uint8)

    for x in range(W):
        for y in range(H):
            new_img[x, y] = img[x, H - 1 - y]

    return np.reshape(new_img, (W, H))

def flipping_horizontal(img):

    W,H = img.shape[:2]

    new_img = np.zeros((W,H), np.uint8)

    for x in range(W):
        for y in range(H):
            new_img[x, y] = img[W - 1 - x, y]

    return np.reshape(new_img, (W, H))

def flipping_titik_asal(img):

    W,H = img.shape[:2]

    new_img = np.zeros((W,H), np.uint8)

    for x in range(W):
        for y in range(H):
            new_img[x, y] = img[W - 1 - x, H -1 -y]

    return np.reshape(new_img, (W, H))



img = cv.imread("benzema.png", 0)
cv.imshow("original", img)
cv.imshow("flipping_vertikal", flipping_vertikal(img))
cv.imshow("flipping_horizontal", flipping_horizontal(img))
cv.imshow("flipping_titik_asal", flipping_titik_asal(img))
cv.waitKey(0)
cv.destroyAllWindows()