import cv2
import numpy as np

pitch_line = ((200, 100), (200, 500))
volume_line = ((700, 600), (1200, 600))

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    cv2.line(frame, pitch_line[0], pitch_line[1], (255, 255, 255), thickness=3)
    cv2.line(frame, volume_line[0], volume_line[1], (255, 255, 255), thickness=3)

    cv2.imshow("Frame", frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
