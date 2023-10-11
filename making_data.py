import cv2
import os
import winsound
from time import sleep

# Takes pictures from webcam and saves them to a folder

folder = r''
num_frames = 4000

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
sleep(5)

for i in range(num_frames):
    ret, frame = cap.read()
    cv2.imwrite(os.path.join(folder, f'image_{i}.jpg'), frame)
    print(i)

cap.release()

winsound.PlaySound('sound.wav', winsound.SND_FILENAME)