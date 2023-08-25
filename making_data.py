import cv2
import os
import winsound
from time import sleep

# Takes pictures from webcam and saves them to a folder

folder = r'C:\Users\rober\Desktop\Programmering\Python\Github\Blink_trackV2\data\open_to_rotate'

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

num_frames = 4000

winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
sleep(5)

for i in range(num_frames):
    ret, frame = cap.read()
    cv2.imwrite(os.path.join(folder, f'imessaesses_{i}.jpg'), frame)
    print(i)

cap.release()

winsound.PlaySound('sound.wav', winsound.SND_FILENAME)