from skimage import io,transform,filters,exposure,data
from matplotlib import pyplot as plt


#----------------open image------------------------
img = io.imread("images/image.jpg")
img1 = io.imread("images/test.jpg", as_gray=True)
#------------------non-Local filter----------------
img_exp = exposure.equalize_hist(img)
img_fg = filters.threshold_otsu(img1)

plt.subplot(221)
plt.title("original image")
plt.imshow(img)
plt.subplot(222)
plt.title("processed image")
plt.imshow(img_exp)
plt.subplot(223)
plt.title("orgimg")
plt.imshow(img1)
plt.subplot(224)
plt.title("processed")
plt.imshow(img_fg)

plt.subplots_adjust(top=1.5, bottom=1, left=0.10, right=.95, hspace=0.25,wspace=0.35)