#KÖR BARA DENNA FIXA BARA TEXTEN I CAMERAN SOM VISAS. TA BORT GLASÖGON!!!!!!!!!!!

import dlib
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from matplotlib import pyplot as plt

tf.config.list_physical_devices('GPU')



model = load_model('best_model_07_31.h5')

# Initialize dlib's face detector and facial landmarks predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

def detect_eyes(frame, gray):
    faces = detector(gray)
    for face in faces:
        landmarks = predictor(gray, face)

        # The coordinates of the left eye
        left_x = landmarks.part(36).x
        left_y = landmarks.part(36).y
        right_x = landmarks.part(39).x
        right_y = landmarks.part(39).y

        # The coordinates of the right eye
        left_x_2 = landmarks.part(42).x
        left_y_2 = landmarks.part(42).y
        right_x_2 = landmarks.part(45).x
        right_y_2 = landmarks.part(45).y

        # Extract the eyes from the image
        left_eye = frame[left_y:right_y, left_x:right_x]
        right_eye = frame[left_y_2:right_y_2, left_x_2:right_x_2]

        for eye, label in [(left_eye, "Left"), (right_eye, "Right")]:
            if eye.size == 0:
                continue
            eye = cv2.resize(eye, (128, 128))
            eye = eye.astype("float") / 255.0
            eye = np.expand_dims(eye, axis=0)
            prediction = model.predict(eye)[0][0]
            if prediction > 0.5:
                text = f"{label} Open"
            else:
                text = f"{label} Closed"
            cv2.putText(frame, text, (left_x, left_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    return frame

# Capture video from the webcam
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect_eyes(frame, gray)
    cv2.imshow('Eye Detection', canvas)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
