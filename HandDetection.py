import cv2
import numpy as np
import time

# import pygame as pg
from synthesizer import Synthesizer, Waveform, player





# face_cascade = cv2.CascadeClassifier('facialdetection.xml')
# palm_cascade = cv2.CascadeClassifier('palm detection.xml')
test_cascade = cv2.CascadeClassifier('closed_frontal_palm.xml')
cam = cv2.VideoCapture(0)

pitch_line = ((200, 100), (200, 500))
volume_line = ((700, 600), (1200, 600))

pg.init()

def draw_lines(frame):
    cv2.line(frame, pitch_line[0], pitch_line[1], (255, 255, 255), 3)
    cv2.line(frame, volume_line[0], volume_line[1], (255, 255, 255), 3)

def play_note2(y):
    RATE = 2000000
    synthesizer = Synthesizer(Waveform.sawtooth, 1.0, False, RATE)
    wave = synthesizer.generate_constant_wave(y, 0.05)
    player_ = player.Player()
    player_.open_stream()

    player_.play_wave(wave)


def play_note(y):

    print(y)
    starty = 70
    height=35
    if (y<starty):
        sound = pg.mixer.Sound("Music_Notes/F_s.wav")
    elif (y<starty+(height*1)):
        sound = pg.mixer.Sound("Music_Notes/G.wav")
    elif (y<starty+(height*2)):
        sound = pg.mixer.Sound("Music_Notes/G_s.wav")
    elif (y<starty+(height*3)):
        sound = pg.mixer.Sound("Music_Notes/A.wav")
    elif (y<starty+(height*4)):
        sound = pg.mixer.Sound("Music_Notes/Bb.wav")
    elif (y<starty+(height*5)):
        sound = pg.mixer.Sound("Music_Notes/B.wav")
    elif (y < starty+(height*6)):
        sound = pg.mixer.Sound("Music_Notes/C1.wav")
    elif (y < starty+(height*7)):
        sound = pg.mixer.Sound("Music_Notes/C_s1.wav")
    elif (y < starty+(height*8)):
        sound = pg.mixer.Sound("Music_Notes/D1.wav")
    elif (y < starty+(height*9)):
        sound = pg.mixer.Sound("Music_Notes/D_s1.wav")
    elif (y < starty+(height*10)):
        sound = pg.mixer.Sound("Music_Notes/E1.wav")
    else:
        sound = pg.mixer.Sound("Music_Notes/F1.wav")


    sound.play()
    sound.play()
    sound.play()




    # wav = SquareTable()
    # beat = Metro(1,1).play()
    # envelope = CosTable([(0, 0), (100, 1), (500, 0.3), (8191, 0)])
    # amplitude = TrigEnv(beat, envelope, 25, 7)
    # pitch = TrigXnoiseMidi(beat, 0, 0.5, 0.5, 0, [0,127], 1, 0)
    # oscillator = Osc(wav, pitch, amplitude).out()
    # oscillator.play()


g=440
while cam.isOpened():


    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # hands = face_cascade.detectMultiScale(gray, 1.09, 5)
    hands = test_cascade.detectMultiScale(gray, 1.14, 5)

    if len(hands)>0:
        h = 0
        for hand in hands:

            if hand[2]>h:
                h = hand[2]
                g = hand[1]
        play_note2(g)


    else:
        play_note2(g)

    # hands = palm_cascade.detectMultiScale(gray, 1.08, 8)
    for (x,y,w,h) in hands:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    draw_lines(img)
    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

cam.release()
cv2.destroyAllWindows()
