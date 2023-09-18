# AI_sleep_tracking
A ai project to track if the user has their eyes closed for too long and then shoots water in the face using a raspberry pi.

## Libraries
* OpenCV
* Numpy
* Tensorflow
* Keras
* Matplotlib

## File structure
GPU_test.py is a test file to see if the GPU is working.

Invert_pictures.py inverts the data to make "more" data.

Main.ipynb is the model that uses cv2 to detect if the eyes are open or closed and then send positions to the servoes to go to.

Making_data.py takes lots of pictures and saves them to a folder.

rotate_pictures.py rotates the data to make "more" data.

Training.ipynb is the ai creating,training and testing.




