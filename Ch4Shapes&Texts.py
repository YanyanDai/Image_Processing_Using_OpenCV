import cv2
import numpy as np 

img = np.zeros((512,512,3), np.uint8) #create image
img[:] = 255, 255, 255

#cv2.circle(img, (256,256), 150,(0,69,255),15)
cv2.circle(img, (256,256), 150,(0,69,255),cv2.FILLED)
#cv2.rectangle(img, (130,226), (382,286), (255,255,255),5)
cv2.rectangle(img, (130,226), (382,286), (255,255,255),cv2.FILLED)
cv2.line(img, (130, 296), (382,296), (255,255,255), 2)

cv2.putText(img, "Summer Workshop", (137,262),cv2.FONT_HERSHEY_DUPLEX, 0.75, (0,69,255), 1)

cv2.imshow("image", img)
cv2.waitKey(0)
