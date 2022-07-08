import cv2
import numpy as np 

img = cv2.imread("Resources/lena.png")
print(img.shape)



cv2.imshow("image", img)
cv2.imshow("image Resize 1", imgResize1)
cv2.imshow("image Resize 2", imgResize2)
cv2.imshow("image Crop", imgCrop)
cv2.waitKey(0)
