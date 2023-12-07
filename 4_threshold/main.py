import cv2
import numpy as np

img = cv2.imread("bookpage.jpg",0)

ret, threshold = cv2.threshold(img,12,255,cv2.THRESH_BINARY)

# OTSU Thresholding
ret2, threshold2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

thresh = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,0.9)

# cv2.imshow("Binary Image",threshold)
# cv2.imshow("Binary Image OTSU",threshold2)
cv2.imshow("Binary Image Adaptive",thresh)
cv2.imshow("Original image",img)


cv2.waitKey(0)
cv2.destroyAllWindows()
