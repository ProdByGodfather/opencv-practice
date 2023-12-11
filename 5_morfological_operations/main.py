import cv2 
import numpy as np

# Import modules
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load image
img = cv2.imread("download.jpg",0)

# threshold on image
_, mask = cv2.threshold(img,130,255,cv2.THRESH_BINARY)

# Erosion (کوچک یا سایش دادن فضا های سفید یا خالی )
kernel = np.ones((3,3),np.uint8)
eroded_image = cv2.erode(mask, kernel, iterations=1)

# Dilation (اضافه کردن یک لایه سفید یا خالی به لایه های سفید یا خالی دیگر)
delated_image = cv2.dilate(mask, kernel, iterations=1)

# Closing (یک دست کردن فضا های خالی)
closed_image = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# Opening


# Gradiant


# Show Image With Plot
fig,(ax1,ax2,ax3,ax4,ax5) = plt.subplots(nrows=1, ncols=5, figsize=(10,20))
cmap_val = "gray"
ax1.axis("off")
ax1.title.set_text('original image')
ax2.axis("off")
ax2.title.set_text('mask')
ax3.axis("off")
ax3.title.set_text('eroded image')
ax4.axis("off")
ax4.title.set_text('dilated image')
ax5.axis("off")
ax5.title.set_text('closed image')
ax1.imshow(img,cmap=cmap_val)
ax2.imshow(mask,cmap=cmap_val)
ax3.imshow(eroded_image,cmap=cmap_val)
ax4.imshow(delated_image,cmap=cmap_val)
ax5.imshow(closed_image,cmap=cmap_val)

plt.show()