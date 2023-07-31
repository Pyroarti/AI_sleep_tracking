from PIL import Image
import os

input_folder = r'C:\Users\rober\Desktop\Programmering\Python\Github\Blink_trackV2\data\open_to_rotate'
output_folder = r'C:\Users\rober\Desktop\Programmering\Python\Github\Blink_trackV2\data\open_rotated'

for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        
        flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)

        flipped_img_path = os.path.join(output_folder, 'flipppfpped'+filename)
        flipped_img.save(flipped_img_path)
