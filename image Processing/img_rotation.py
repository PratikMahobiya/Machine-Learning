from skimage import io,transform,filters
from matplotlib import pyplot as plt


#----------------open image------------------------
img = io.imread("images/image.jpg")
img2 = io.imread("images/image.jpg", as_gray=True)

#------------Processing - Rotation-----------------
img_90 = transform.rotate(img, 90)
img_180 = transform.rotate(img, 180)
img_270 = transform.rotate(img, 270)
img_360 = transform.rotate(img, 360)

#--------------edge Detection----------------------
img_rob = filters.roberts(img2)
img_sob = filters.sobel(img2)

#-------------plotting image------------------------
plt.subplot(321)
plt.title("90 degre")
plt.imshow(img_90)
plt.subplot(322)
plt.title("180 degre")
plt.imshow(img_180)
plt.subplot(323)
plt.title("270 degre")
plt.imshow(img_270)
plt.subplot(324)
plt.title("360 degre")
plt.imshow(img_360)



plt.subplots_adjust(top=1.5, bottom=0.08, left=0.10, right=.95, hspace=0.25,wspace=0.35)