from cvzone.HandTrackingModule import HandDetector
from cvzone.SerialModule import SerialObject
import cv2

serialObject = SerialObject("COM5", baudRate=9600, digits=1)

curr_status = [1, 1, 1, 1, 1]
serialObject.sendData(curr_status)

def hand_tracker():
    cap = cv2.VideoCapture(0)

    detector = HandDetector(maxHands=2, detectionCon=0.8)
    mode = ""
    data = ""

    def image_read():
        success, img = cap.read()
        hands, img = detector.findHands(img)

        if hands:
            hand = hands[0]
            
            fingers = detector.fingersUp(hand)
            serialObject.sendData(fingers)
            print(fingers)

        cv2.imshow("Capture", img)
        cv2.waitKey(1)
    while True:
        image_read()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def manual_changer(idx):
    global curr_status
    curr_status[idx] = 1 - curr_status[idx]
    serialObject.sendData(curr_status)
