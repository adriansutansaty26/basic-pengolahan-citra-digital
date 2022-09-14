import cv2

src = "soekarno.jpg"
img = cv2.imread(src)
img_gray = cv2.imread(src,0)

t = 128
H,W = img_gray.shape[:2]

img_penjumlahan = img_gray.copy()
img_pengurangan = img_gray.copy()
skalar = 70

for i in range(H):
    for j in range(W):
        pixel = img_penjumlahan[i, j] + skalar
        if pixel > 255:
            img_penjumlahan[i, j] = 255
        else:
            img_penjumlahan[i, j] = pixel
            
            
for i in range(H):
    for j in range(W):
        pixel = img_pengurangan[i, j] - skalar
        if pixel < 0:
            img_pengurangan[i, j] = 0
        else:
            img_pengurangan[i, j] = pixel

cv2.imshow("original",img_gray)
cv2.imshow("img_penjumlahan",img_penjumlahan)
cv2.imshow("img_pengurangan",img_pengurangan)
cv2.waitKey(0)
cv2.destroyAllWindows()