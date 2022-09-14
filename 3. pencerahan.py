import cv2

src = "benzema.png"
img = cv2.imread(src)
img_gray = cv2.imread(src,0)

t = 128
H,W = img_gray.shape[:2]

img_brighten = img_gray.copy()
bright = 70 # skalar pencerah

for i in range(H):
    for j in range(W):
        pixel = img_brighten[i, j] + bright
        if pixel > 255:
            img_brighten[i, j] = 255
        else:
            img_brighten[i, j] = pixel

cv2.imshow("original",img)
cv2.imshow("grayscale",img_gray)
cv2.imshow("brighten",img_brighten)
cv2.waitKey(0)
cv2.destroyAllWindows()