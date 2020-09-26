import cv2
import numpy as np
import imutils


def nothing(x):
    pass

img = cv2.imread("template/plt.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canvas = np.zeros(img.shape, np.uint8)

cv2.namedWindow("Adjust")
cv2.createTrackbar("l_H", "Adjust", 0,180,nothing)
cv2.createTrackbar("l_S", "Adjust", 0,180,nothing)
cv2.createTrackbar("l_V", "Adjust", 0,180,nothing)
cv2.createTrackbar("U_H", "Adjust", 240,255,nothing)
cv2.createTrackbar("U_S", "Adjust", 240,255,nothing)
cv2.createTrackbar("U_V", "Adjust", 240,255,nothing)
# cv2.createTrackbar("L_TH", "Adjust", 100,300,nothing)


while True:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    l_H = cv2.getTrackbarPos("l_H", "Adjust")
    l_S = cv2.getTrackbarPos("l_S", "Adjust")
    l_V = cv2.getTrackbarPos("l_V", "Adjust")
    U_H = cv2.getTrackbarPos("U_H", "Adjust")
    U_S = cv2.getTrackbarPos("U_S", "Adjust")
    U_V = cv2.getTrackbarPos("U_V", "Adjust")
    L_TH = cv2.getTrackbarPos("L_TH", "Adjust")

    lower_silver = np.array([l_H,l_S,l_V])
    upper_silver = np.array([U_H,U_S,U_V])

    # lower_silver = np.array([0,0,154])
    # upper_silver = np.array([255,255,225])

    mask = cv2.inRange(hsv, lower_silver,upper_silver)
    edge = cv2.Canny(mask, L_TH, 300)
    kernel = np.ones((5,5),np.uint8)
    # mask = cv2.dilate(mask, kernel, iterations=1)
    # mask = cv2.erode(edge, kernel, iterations=1)
    # mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN , kernel)
    # mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE , kernel)

    cv2.imshow("mask",cv2.resize(edge, None, fx = 0.5, fy = 0.5))
    key = cv2.waitKey(1)
    if key == 27:
        break

cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
    

for c in cnts:
    (x, y, w, h) = cv2.boundingRect(c)

    if (80>=w<=100) and (50>=h<=100):
        cv2.rectangle(canvas, (x, y), (x + w, y + h), (0, 255, 0), 2)
    

#Calculate ---------------------------------------------------------- 
canvas2gray = cv2.cvtColor(canvas,cv2.COLOR_BGR2GRAY)

im2,contours,hierarchy = cv2.findContours(canvas2gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("Number of boxes:-",len(contours)-1)

cv2.imshow("canvas",cv2.resize(canvas, None, fx = 0.5, fy = 0.5))
cv2.waitKey(0)

cv2.destroyAllWindows()