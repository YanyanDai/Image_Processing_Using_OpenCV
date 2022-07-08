import cv2
import numpy as np 

img = cv2.imread("Resources/lena.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 5)
imgCanny = cv2.Canny(imgBlur,100,120)
kernel = np.ones((5,5),np.uint8)
imgDia = cv2.dilate(imgCanny,kernel, iterations=1)
imgErode = cv2.erode(imgDia,kernel, iterations=1)

cv2.imshow("output", img)
cv2.imshow("image Gray", imgGray)
cv2.imshow("image Blur", imgBlur)
cv2.imshow("image Canny", imgCanny)
cv2.imshow("image Dilation", imgDia)
cv2.imshow("image Erode", imgErode)
cv2.waitKey(0)