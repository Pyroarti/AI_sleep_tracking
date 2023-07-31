import cv2
import os
import winsound
from time import sleep

# Folder to save the images
folder = r'C:\Users\rober\Desktop\Programmering\Python\Github\Blink_trackV2\data\open_to_rotate'

# Create the folder if it doesn't exist
if not os.path.exists(folder):
    os.makedirs(folder)

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Set the width and height
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Number of frames to capture
num_frames = 4000

winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
sleep(5)

for i in range(num_frames):
    ret, frame = cap.read()
    cv2.imwrite(os.path.join(folder, f'imessaesses_{i}.jpg'), frame)
    print(i)

cap.release()

winsound.PlaySound('sound.wav', winsound.SND_FILENAME)