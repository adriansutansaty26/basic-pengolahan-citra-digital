import numpy as np
import cv2 as cv

img = cv.imread('benzema.png',0)

sobelx64f = cv.Sobel(img,cv.CV_64F,1,0,ksize=3)
sobely64f = cv.Sobel(img,cv.CV_64F,0,1,ksize=3)

magnitudesobel = cv.magnitude(sobelx64f,sobely64f)
abs_sobel64f = np.absolute(magnitudesobel)
sobel_8u = np.uint8(abs_sobel64f)

cv.imshow('Original', img)
cv.imshow('Sobel Magnitude', sobel_8u)
cv.waitKey(0)
cv.destroyAllWindows()