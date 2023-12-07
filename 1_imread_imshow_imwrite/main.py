# import moduels

import cv2
import numpy as np
from matplotlib import pyplot as plt

# read image
img = cv2.imread("logo.png", 0)

# show image and wait for any key to close image preview
# cv2.imshow("Image View",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

plt.imshow(img,cmap='gray',interpolation="bicubic")
plt.xticks([]), plt.yticks([])
plt.plot([10,10],[240,240],linewidth=5)
plt.show()


# save gray color image as file_export.png to base dir
# cv2.imwrite("file_export.png",img)