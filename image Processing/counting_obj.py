import cv2
from skimage.metrics import structural_similarity
from skimage.feature import peak_local_max
import imutils
from scipy import ndimage
import numpy as np
from matplotlib import pyplot as plt


# load the two input images------------------------------------------
img_1 = cv2.imread("template/test1.jpeg")
# Blank camvas  
canvas = np.zeros(img_1.shape, np.uint8)

# convert the images to grayscale------------------------------------
grayA = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)

kernel = np.ones((5,5),np.uint8)
kernel2 = np.ones((5,5),np.uint8)

# threshold the difference image, followed by finding contours to----
# obtain the regions of the two input images that differ-------------
thresh_otsu = cv2.threshold(grayA, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
D = ndimage.distance_transform_edt(thresh_otsu.copy())


dilation = cv2.erode(thresh_otsu,kernel,iterations = 1)
opening = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)

cnts = cv2.findContours(opening.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
    

for c in cnts:
 	# compute the bounding box of the contour and then draw the------
 	# bounding box on both input images to represent where the two
 	# images differ--------------------------------------------------
 	(x, y, w, h) = cv2.boundingRect(c)
 	cv2.rectangle(canvas, (x, y), (x + w, y + h), (0, 255, 0), 2)

#Calculate ---------------------------------------------------------- 
canvas2gray = cv2.cvtColor(canvas,cv2.COLOR_BGR2GRAY)

im2,contours,hierarchy = cv2.findContours(canvas2gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("Number of Matched Emojies:-",len(contours)-1)

    
# show the output images---------------------------------------------
cv2.imshow("Original", cv2.resize(img_1, None, fx = 0.9, fy = 0.9))
cv2.imshow("Canvas", cv2.resize(canvas, None, fx = 0.9, fy = 0.9))
cv2.imshow("thresh_otsu", cv2.resize(thresh_otsu, None, fx = 0.9, fy = 0.9))
cv2.imshow("dilation", cv2.resize(dilation, None, fx = 0.9, fy = 0.9))
cv2.imshow("opening", cv2.resize(opening, None, fx = 0.9, fy = 0.9))
cv2.imshow("D image", D)
cv2.waitKey(0)
cv2.destroyAllWindows()
