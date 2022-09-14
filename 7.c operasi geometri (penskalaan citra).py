import numpy as np
import cv2 as cv
from scipy.ndimage import zoom


def clipped_zoom(img, zoom_factor):

    h, w = img.shape[:2]

    zoom_tuple = (zoom_factor, ) * 2 + (1,) * (img.ndim - 2)

    # Zoom out
    if zoom_factor < 1:

        # Menetapkan box region zoom gambar
        zh = int(np.round(h * zoom_factor))
        zw = int(np.round(w * zoom_factor))
        top = (h - zh) // 2
        left = (w - zw) // 2

        # Menghapus piksel padding
        out = np.zeros_like(img)
        out[top:top+zh, left:left+zw] = zoom(img, zoom_tuple, )

    # Zoom in
    elif zoom_factor > 1:

        # Menetapkan box region zoom gambar
        zh = int(np.round(h / zoom_factor))
        zw = int(np.round(w / zoom_factor))
        top = (h - zh) // 2
        left = (w - zw) // 2

        out = zoom(img[top:top+zh, left:left+zw], zoom_tuple, )

        # Menghapus piksel tambahan
        trim_top = ((out.shape[0] - h) // 2)
        trim_left = ((out.shape[1] - w) // 2)
        out = out[trim_top:trim_top+h, trim_left:trim_left+w]

    else:
        out = img
        
    return out


img = cv.imread('benzema.png')
cv.imshow("original", img)
cv.imshow("result", clipped_zoom(img, 2, ))
cv.waitKey(0)
cv.destroyAllWindows()