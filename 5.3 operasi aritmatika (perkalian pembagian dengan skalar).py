import cv2

src = "soekarno.jpg"
img = cv2.imread(src)
img_gray = cv2.imread(src,0)

t = 128
H,W = img_gray.shape[:2]

img_perkalian = img_gray.copy()
img_pembagian = img_gray.copy()
skalar = 5

for i in range(H):
    for j in range(W):
        pixel = img_perkalian[i, j] * skalar
        if pixel > 255:
            img_perkalian[i, j] = 255
        elif pixel < 0:
            img_perkalian[i, j] = 0
        else:
            img_perkalian[i, j] = pixel

for i in range(H):
    for j in range(W):
        pixel = img_pembagian[i, j] / skalar
        if pixel > 255:
            img_pembagian[i, j] = 255
        elif pixel < 0:
            img_pembagian[i, j] = 0
        else:
            img_pembagian[i, j] = pixel


cv2.imshow("original",img_gray)
cv2.imshow("img_perkalian",img_perkalian)
cv2.imshow("img_pembagian",img_pembagian)
cv2.waitKey(0)
cv2.destroyAllWindows()