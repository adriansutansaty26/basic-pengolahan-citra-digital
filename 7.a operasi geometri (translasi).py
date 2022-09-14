import numpy as np
import cv2 as cv
from PIL import Image

def translasi(m, n):
    src = "benzema.png"
    img = cv.imread(src,0)

    W,H = img.shape[:2]

    new_img = np.zeros((W,H), np.uint8)
    

    start_m = m
    start_n = n

    if m < 0:
        start_m = 0
    if n < 0:
        start_n = 0

    for x in range(start_m, W):
        for y in range(start_n, H):
            new_x = x - m
            new_y = y - n
       
            if (new_x >= W or new_y >= H or new_x < 0 or new_y < 0):
                new_img[x, y] = 0
            else:
                new_img[x, y]= img[new_x, new_y]
                
                
    new_img = np.reshape(new_img, (W, H))
    cv.imshow("original", img)
    cv.imshow("translasi", new_img)
    cv.waitKey(0)
    cv.destroyAllWindows()
                        

translasi(-20, 20)