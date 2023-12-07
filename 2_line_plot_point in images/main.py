# import modules
import cv2
import numpy as np



img = cv2.imread("logo.png",1)


# Line Have Many Args (1: start position, 2: end position, 3: color(B,G,R), 4: line width)
cv2.line(img,(5,5),(200,200),(55,200,0), 5)
# rectangle Have Many Args (1: start position, 2: end position, 3: color(B,G,R), 4: line width)
cv2.rectangle(img,(80,90),(200,180),(0,0,100),3)
# circle Have Many Args (1: start position, 2: end position, 3: color(B,G,R), 4: line width)
cv2.circle(img, (100,50), 50, (0,255,255),-1)

points = np.array([[30,50],[40,76],[200,100]],np.int32)
cv2.polylines(img,[points],True,(0,0,255),4)

# write text on image
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,"Hello Mother Fucker",(150,12), font,.4 ,(255,255,255),1,cv2.LINE_AA)


# cv2.imwrite("logo_changed.png",img)
   
cv2.imshow("Abar Vision",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
