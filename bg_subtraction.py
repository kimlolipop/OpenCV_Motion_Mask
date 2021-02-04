import cv2

#ใช่แบบนี้ไม่ต้องเก็บ buffer เอง
cap = cv2.VideoCapture('D:\Super AI Level 2\Week4\Denso\Dataset\Video\CtlEquip_10_4883_20200416081455.mp4')
# bgsubknn = cv2.createBackgroundSubtractorKNN(10) # มักจะดีกว่า , กำหนดเก็บ 10 frame
# bgsubmog = cv2.createBackgroundSubtractorMOG2(10)

bgsubknn = cv2.createBackgroundSubtractorKNN() # มักจะดีกว่า , default จะเก็บ buffer 400 - 500 grame
bgsubmog = cv2.createBackgroundSubtractorMOG2()
while True:
    ret, frame = cap.read()


    img = frame[0:200, 480:700] # Y, X
    if not ret:
        break
    fgknn = bgsubknn.apply(frame)
    fgmog = bgsubmog.apply(frame)

    cv2.imshow('fre', img)
    cv2.imshow('frame', frame)
    cv2.imshow('fgknn', fgknn)
    cv2.imshow('fgmog', fgmog)
    cv2.waitKey(1)
