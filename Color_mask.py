import cv2
import numpy as np

def nothing(x):
    pass


cap = cv2.VideoCapture('20200413\CtlEquipSum_1\CtlEquipSum_1_177587_20200413083647.mp4')

# frame_counter = 0
# frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
# loop_flag = 0
# pos = 0


# cv2.namedWindow('video')
# cv2.createTrackbar('time', 'video', 0, frames, nothing)

# cv2.namedWindow("Trackbars")
# cv2.createTrackbar("L - H", "Trackbars", 0, 180, nothing)
# cv2.createTrackbar("L - L", "Trackbars", 0, 255, nothing)
# cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
# cv2.createTrackbar("U - H", "Trackbars", 0, 180, nothing)
# cv2.createTrackbar("U - L", "Trackbars", 0, 255, nothing)
# cv2.createTrackbar("U - S", "Trackbars", 0, 255, nothing)


while True:
    # if loop_flag == pos:
    #     loop_flag = loop_flag + 1
    #     cv2.setTrackbarPos('time', 'video', loop_flag)
    # else:
    #     pos = cv2.getTrackbarPos('time', 'video')
    #     loop_flag = pos
    #     cap.set(cv2.CAP_PROP_POS_FRAMES, pos)




    ret, raw_frame = cap.read()
    # img = frame[100:160, 390:490] # Y, X

    hsv = cv2.cvtColor(raw_frame[110:160, 390:490], cv2.COLOR_BGR2HLS)

    # l_H = cv2.getTrackbarPos("L - H", "Trackbars")
    # l_L = cv2.getTrackbarPos("L - L", "Trackbars")
    # l_S = cv2.getTrackbarPos("L - S", "Trackbars")
    # u_H = cv2.getTrackbarPos("U - H", "Trackbars")
    # u_L = cv2.getTrackbarPos("U - L", "Trackbars")
    # u_S = cv2.getTrackbarPos("U - S", "Trackbars")
    
    lower_blue = np.array([0, 79, 84])
    upper_blue = np.array([180, 255, 255])

    mask = cv2.inRange(hsv,lower_blue, upper_blue)

    cv2.imshow('mask', mask)
    cv2.imshow('fre', raw_frame)
    cv2.imshow('crop', raw_frame[110:160, 390:490])


    # if cv2.waitKey(30) & loop_flag == frames:
    #   break
    cv2.waitKey(30)


