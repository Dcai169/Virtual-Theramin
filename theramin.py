import cv2
import numpy as np
import grip
from random import randint

pitch_line = ((200, 100), (200, 500))
volume_line = ((700, 600), (1200, 600))

cap = cv2.VideoCapture(0)
pipeline = grip.GripPipeline()

def get_rand_color() -> (int, int, int):
    return randint(0, 255), randint(0, 255), randint(0, 255)

while True:
    _, frame = cap.read()

    pipeline.process(frame)
    blobs = pipeline.find_blobs_output

    cv2.drawKeypoints(frame, blobs, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.line(frame, pitch_line[0], pitch_line[1], (255, 255, 255), thickness=3)
    cv2.line(frame, volume_line[0], volume_line[1], (255, 255, 255), thickness=3)

    if len(blobs) is not 0:
        # print(f"{blobs[len(blobs)-1].pt}")
        for blob in blobs:
            cv2.circle(frame, (int(blob.pt[0]), int(blob.pt[1])), int(blob.size), (255, 255, 255), thickness=4)

    cv2.imshow("Frame", frame)


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
