import cv2
import numpy as np
import threading
from synthesizer import Synthesizer, Waveform, player


# face_cascade = cv2.CascadeClassifier('facialdetection.xml')
# palm_cascade = cv2.CascadeClassifier('palm detection.xml')
test_cascade = cv2.CascadeClassifier('closed_frontal_palm.xml')
cam = cv2.VideoCapture(0)

pitch_line = ((200, 100), (200, 500))
volume_line = ((700, 600), (1200, 600))


def draw_lines(frame):
    cv2.line(frame, pitch_line[0], pitch_line[1], (255, 255, 255), 3)
    cv2.line(frame, volume_line[0], volume_line[1], (255, 255, 255), 3)




def play_note2(y):
    RATE = 20000
    synthesizer = Synthesizer(Waveform.sawtooth, 0.003, False, RATE)
    wave = synthesizer.generate_constant_wave(1000-y, 1)
    player_ = player.Player()
    player_.open_stream()

    player_.play_wave(wave)


g = 440

while cam.isOpened():
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # hands = face_cascade.detectMultiScale(gray, 1.09, 5)
    hands = test_cascade.detectMultiScale(gray, 1.14, 5)

    if len(hands) > 0:
        h = 0
        for hand in hands:
            if hand[2] > h:
                h = hand[2]
                g = hand[1]

        tnote = threading.Thread(None, target=play_note2, args=(g,))
        tnote.start()

    # hands = palm_cascade.detectMultiScale(gray, 1.08, 8)
    for (x, y, w, h) in hands:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    draw_lines(img)
    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xff
    if k is 27:
        break

cam.release()
cv2.destroyAllWindows()
