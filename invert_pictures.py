from PIL import Image
import os

# Takes all images in a folder and inverts them to make more data

input_folder = r''
output_folder = r''

for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        
        flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)

        flipped_img_path = os.path.join(output_folder, 'flipped'+filename)
        flipped_img.save(flipped_img_path)
