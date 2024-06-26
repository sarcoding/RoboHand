def hand_tracker():
    from cvzone.HandTrackingModule import HandDetector
    from cvzone.SerialModule import SerialObject
    import cv2
    cap = cv2.VideoCapture(0)

    detector = HandDetector(maxHands=2, detectionCon=0.8)
    serialObject = SerialObject("COM5", baudRate=9600, digits=1)
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
