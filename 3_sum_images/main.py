import cv2
import numpy as np

img1 = cv2.imread("1.jpg",0)
img2 = cv2.imread('2.jpg',0)

# img3 = img1 + img2   
# img3 = cv2.add(img1,img2)
# img3 = cv2.addWeighted(img1, 0.4,img2,0.6,0)
ref, mask = cv2.threshold(img1,200,255,cv2.THRESH_BINARY)
reverse = cv2.bitwise_not(mask)
# masks
# cv2.imshow("The Mask", mask)
# cv2.imshow("The Mask reversed", reverse)

img_m = cv2.bitwise_and(img2,img2,mask=mask)
img_r = cv2.bitwise_and(img2,img2,reverse)
end_img = cv2.add(img_m,img_r)
cv2.imshow("bitwise",end_img)
# img_m = cv2.bitwise_and(img2,img2,mask=reverse)
# cv2.imshow("bitwise and",img_m)
# cv2.imshow("image 2",img2)


cv2.waitKey(0)
cv2.destroyAllWindows()