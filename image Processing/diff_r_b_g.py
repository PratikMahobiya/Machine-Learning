import cv2
import numpy as np
from matplotlib import pyplot as plt

img_1 = cv2.imread("images/red.png")
img_2 = cv2.imread("images/red3.jpg")

# -----------------check both img size ------------------------------
if img_1.shape == img_2.shape:
    print("The images have same size and channels")
    difference = cv2.subtract(img_1,img_2)
    b, g, r = cv2.split(difference)
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("The images are completely Equal")
    else:
        print("The Images are not same..")
else:
    print("Images Have not same size")
        

# ----------------Check for similarities---------------------------
sift = cv2.xfeatures2d.SIFT_create()
kp_1, desc_1 = sift.detectAndCompute(img_1, None)
kp_2, desc_2 = sift.detectAndCompute(img_2, None)

print(sift)


index_params = dict(algorithm=0, trees=5)
search_params = dict()
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(desc_1, desc_2, k=2)
print(len(matches))


good_points = []
ratio = 0.6
for m, n in matches:
    if m.distance < ratio*n.distance:
        good_points.append(m)
print(len(good_points))
        
        
result = cv2.drawMatches(img_1, kp_1, img_2, kp_2,good_points, None)

# plt.subplot(321)
# plt.title("Img_1")
# plt.imshow(img_1)
# plt.subplot(322)
# plt.title("Img_2")
# plt.imshow(img_2)
# plt.subplot(323)
# # plt.title("Img_2")
# # plt.imshow(result)

cv2.imshow("Original", img_1)
cv2.imshow("Duplicate", img_2)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()