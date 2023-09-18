from scipy import ndimage, misc
import numpy as np
import os
import cv2
import imageio

def main():
    """
    Rotates images in a folder and saves them to a new folder
    """
    outPath = r""
    path = r""

    for image_path in os.listdir(path):

        input_path = os.path.join(path, image_path)
        image_to_rotate = imageio.imread(input_path)

        rotated = ndimage.rotate(image_to_rotate, 45)

        fullpath = os.path.join(outPath, 'rotated45_'+image_path)
        imageio.imwrite(fullpath, rotated)

if __name__ == '__main__':
    main()