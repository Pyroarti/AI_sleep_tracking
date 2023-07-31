from scipy import ndimage, misc
import numpy as np
import os
import cv2
import imageio

def main():
    outPath = r"C:\Users\rober\Desktop\Programmering\Python\Github\Blink_tracking\data2\90"
    path = r"C:\Users\rober\Desktop\Programmering\Python\Github\Blink_tracking\data2\Closed"

    for image_path in os.listdir(path):

        input_path = os.path.join(path, image_path)
        image_to_rotate = imageio.imread(input_path)

        rotated = ndimage.rotate(image_to_rotate, 90)

        fullpath = os.path.join(outPath, 'rotated09_'+image_path)
        imageio.imwrite(fullpath, rotated)

if __name__ == '__main__':
    main()