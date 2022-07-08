import cv2
import numpy as np 



cv2.imshow("output", img)
cv2.imshow("image Gray", imgGray)
cv2.imshow("image Blur", imgBlur)
cv2.imshow("image Canny", imgCanny)
cv2.imshow("image Dilation", imgDia)
cv2.imshow("image Erode", imgErode)
cv2.waitKey(0)
