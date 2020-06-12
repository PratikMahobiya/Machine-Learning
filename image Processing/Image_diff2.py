import cv2
from skimage.metrics import structural_similarity
import imutils
import numpy as np
from matplotlib import pyplot as plt


# load the two input images
img_1 = cv2.imread("images/card.jpg")
img_2 = cv2.imread("images/card2.jpg")

#-----------------check both img size ----------------------------------
if img_1.shape == img_2.shape:
    
    print("The images have same size and channels")
    print("Processing...")
    difference = cv2.subtract(img_1,img_2)
    b, g, r = cv2.split(difference)
    
    # convert the images to grayscale
    grayA = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY)
    
    # compute the Structural Similarity Index (SSIM) between the two----
    # images, ensuring that the difference image is returned------------
    (score, diff) = structural_similarity(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0 and score == 1:
        print("The images are completely Equal")
        print("Similarities Percentage:- {} %".format(score * 100))
        
    elif score > 0.5:
        print("The Images are not Completely Equal..")
        print("Similarities Percentage:- {:.2f} %".format(score * 100))
        
        Inp = input("Do You Want to see difference Comparision (y/n):- ")
        
        if Inp == "y":
            print("Processing...")
            # ----------------Check for similarities---------------------------
            sift = cv2.xfeatures2d.SIFT_create()
            kp_1, desc_1 = sift.detectAndCompute(img_1, None)
            kp_2, desc_2 = sift.detectAndCompute(img_2, None)
            
            
            index_params = dict(algorithm=0, trees=5)
            search_params = dict()
            flann = cv2.FlannBasedMatcher(index_params, search_params)
            matches = flann.knnMatch(desc_1, desc_2, k=2)
            # print(len(matches))
            
            good_points = []
            ratio = 0.7
            for m, n in matches:
                if m.distance < ratio*n.distance:
                    good_points.append(m)
                    
            # print("Completely Matched Points:- "+ str(len(good_points)))
                    
                    
            result = cv2.drawMatches(img_1, kp_1, img_2, kp_2,good_points, None)
            
            # show the output images------------------------------------------
            cv2.imshow("Original", cv2.resize(img_1, None, fx = 0.9, fy = 0.9))
            cv2.imshow("Img To Be Compared", cv2.resize(img_2, None, fx = 0.9, fy = 0.9))
            cv2.imshow("Difference", cv2.resize(diff, None, fx = 0.9, fy = 0.9))
            cv2.imshow("Comparision", cv2.resize(result, None, fx = 0.9, fy = 0.9))
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("Thank you")
        
    else:
        print("Similarities Percentage:- {:.2f} %".format(score * 100))
        print("The Images Are completely Different..")                  
else:
    print("Images Have not same size\nPlease Input TheSame Size Images...")
        