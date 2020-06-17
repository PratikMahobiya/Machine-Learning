import numpy as np
import cv2


img = cv2.imread('template/n_temp.jpg')
canvas = np.zeros(img.shape, np.uint8)
img2gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(img2gray,127,255,cv2.THRESH_BINARY_INV)
im2,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

print(len(contours))

for cont in contours:
    cv2.drawContours(canvas, cont, -1, (0, 255, 0), 3)

cv2.imshow('contours',canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()