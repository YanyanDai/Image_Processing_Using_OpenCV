import cv2
import numpy as np 

img = cv2.imread("Resources/lena.png")
print(img.shape)

imgResize1 = cv2.resize(img,(640,480))
imgResize2 = cv2.resize(img,(0,0),None,0.5,0.5) #scale down
print(imgResize2.shape)

imgCrop = img[100:200,200:300]

cv2.imshow("image", img)
cv2.imshow("image Resize 1", imgResize1)
cv2.imshow("image Resize 2", imgResize2)
cv2.imshow("image Crop", imgCrop)
cv2.waitKey(0)