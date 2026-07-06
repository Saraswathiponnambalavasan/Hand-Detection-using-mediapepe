import mediapipe as mp
import cv2
import pyautogui

hand_detector = mp.solutions.hands.Hands()

draw_landmarks = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    f_h, f_w = frame.shape[:2]
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands=output.multi_hand_landmarks
    l=[]
    if hands:
        for hand in hands:
            draw_landmarks.draw_landmarks(frame, hand)

            for i, landmark in enumerate(hand.landmark):
                x = int(landmark.x * f_w)
                y = int(landmark.y * f_h)

                l.append((i, x, y))

                if i == 8:
                    cv2.circle(frame, (x, y), 5, (255, 0, 255), 5)
                    pyautogui.moveTo(x, y)


    if len(l) >= 9:
        if l[8][2] < l[6][2]:
            print("open")
        else:
            print("close")
    cv2.imshow("Frame", frame)
    cv2.waitKey(1)
