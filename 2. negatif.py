import cv2

src = "benzema.png"
img = cv2.imread(src)
img_gray = cv2.imread(src,0)

t = 128
H,W = img_gray.shape[:2]
img_negative = img_gray.copy()

for i in range(H):
    for j in range(W):
        img_negative[i, j] = 255 - img_negative[i, j]

cv2.imshow("original",img)
cv2.imshow("grayscale",img_gray)
cv2.imshow("negative",img_negative)
cv2.waitKey(0)
cv2.destroyAllWindows()