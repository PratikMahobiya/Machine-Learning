from skimage import io,transform,filters
from matplotlib import pyplot as plt


#----------------open image------------------------
img = io.imread("images/image.jpg", as_gray=True)

#--------------edge Detection----------------------
img_rob = filters.roberts(img)
img_sob = filters.sobel(img)
img_sh  = filters.scharr(img)

#-------------plotting image------------------------
plt.subplot(321)
plt.title("rob-edge detection")
plt.imshow(img_rob)
plt.subplot(322)
plt.title("sob-edge detection")
plt.imshow(img_sob)
plt.subplot(323)
plt.title("schar-edge detection")
plt.imshow(img_sh)

plt.subplots_adjust(top=1.5, bottom=0.08, left=0.10, right=.95, hspace=0.25,wspace=0.35)
