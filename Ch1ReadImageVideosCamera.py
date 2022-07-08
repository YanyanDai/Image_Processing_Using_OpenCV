#import cv2
#print(cv2.__version__)

#### Importing an image
# img = cv2.imread("Resources/shapes.png")
# cv2.imshow('image', img)
# cv2.waitKey(0) #0 infinity 1:1 second



# #### import video
# import cv2
# frameWidth = 640
# frameHeight = 480
# cap = cv2.VideoCapture("Resources/test_video.mp4")

# while True:
#     success, img = cap.read()
#     img = cv2.resize(img,(frameWidth,frameHeight))
#     cv2.imshow("Result", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

####run webcam
import cv2
frameWidth = 640
frameHeight = 480
camSet = "nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int)640, height=(int)480, format=(string)NV12, framerate=(fraction)30/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink"
cap = cv2.VideoCapture(camSet)

while True:
    success, img = cap.read()
    img = cv2.resize(img,(frameWidth,frameHeight))
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break