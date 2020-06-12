from skimage import io
import numpy as np
from matplotlib import pyplot as plt

my_img = io.imread("images/test.jpg")

my_img2 = io.imread("images/test2.jpg")

print(my_img.mean())
print(my_img2.mean())


plt.subplot(2,2,1)
plt.imshow(my_img)
plt.subplot(2,2,3)
plt.imshow(my_img2)