# Python program to illustrate  
# template matching 
import cv2 
import numpy as np 
  
# Read the main image 
img_rgb = cv2.imread('template/1.jpeg')
cpy_img = img_rgb.copy()
# Read the template 
temp = cv2.imread('template/1_temp.jpeg') 
# Blank camvas  
canvas = np.zeros(img_rgb.shape, np.uint8)


# Convert it to grayscale 
img2gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY) 
template = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
# Store width and height of template in w and h 
w, h = template.shape[::-1] 
  
# Perform match operations. 
res = cv2.matchTemplate(img2gray,template,cv2.TM_CCOEFF_NORMED) 
  
# Specify a threshold 
threshold = 0.9
  
# Store the coordinates of matched area in a numpy array 
loc = np.where( res >= threshold)  
  
# Draw a rectangle around the matched region. 
for pt in zip(*loc[::-1]): 
    cv2.rectangle(cpy_img, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
    cv2.rectangle(canvas, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
    
#Calculating the matched part. 
canvas2gray = cv2.cvtColor(canvas,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(canvas2gray,127,255,cv2.THRESH_BINARY_INV)
im2,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("Number of Matched Emojies:-",len(contours)-1)
    

# Show the final image with the matched area. 
cv2.imshow('original',cv2.resize(img_rgb, None, fx = 0.5, fy = 0.5))
cv2.imshow("Detected",cv2.resize(cpy_img, None, fx = 0.5, fy = 0.5))
cv2.imshow('Blueprint',cv2.resize(canvas, None, fx = 0.5, fy = 0.5))
# cv2.imwrite("template/n_temp.jpg", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()