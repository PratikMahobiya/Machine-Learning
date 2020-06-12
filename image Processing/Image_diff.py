import cv2
from skimage.metrics import structural_similarity
import imutils
import numpy as np
from matplotlib import pyplot as plt


# load the two input images
img_1 = cv2.imread("images/red2.jpg")
img_2 = cv2.imread("images/red3.jpg")

#-----------------check both img size ----------------------------------
if img_1.shape == img_2.shape:
    
    print("The images have same size and channels")
    print("Processing...")
    difference = cv2.subtract(img_1,img_2)
    b, g, r = cv2.split(difference)
    
    # convert the images to grayscale-----------------------------------
    grayA = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY)
    
    # compute the Structural Similarity Index (SSIM) between the two----
    # images, ensuring that the difference image is returned------------
    (score, diff) = structural_similarity(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0 and score == 1:
        print("The images are completely Equal")
        print("Similarities Percentage:- {}".format(score * 100))
        
    elif score > 0.5:
        print("The Images are not Completely Equal..")
        print("Processing...")
        
        # threshold the difference image, followed by finding contours to
        # obtain the regions of the two input images that differ---------
        thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        
        print("Similarities Percentage:- {}".format(score * 100))
        
        for c in cnts:
        	# compute the bounding box of the contour and then draw the---
        	# bounding box on both input images to represent where the two
        	# images differ-----------------------------------------------
        	(x, y, w, h) = cv2.boundingRect(c)
        	cv2.rectangle(img_1, (x, y), (x + w, y + h), (0, 0, 255), 2)
        	cv2.rectangle(img_2, (x, y), (x + w, y + h), (0, 0, 255), 2) 
        # show the output images------------------------------------------
        cv2.imshow("Original", img_1)
        cv2.imshow("Modified", img_2)
        cv2.imshow("Diff", diff)
        cv2.imshow("Thresh", thresh)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    else:
        print("Similarities Percentage:- {}".format(score * 100))
        print("The Images Are completely Different..")                  
else:
    print("Images Have not same size\nPlease Input TheSame Size Images...")
        