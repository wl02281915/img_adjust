import os
import shutil
from PIL import Image, ImageEnhance, ImageOps

# Define original and new directories
ori_path = './img_save/'
save_path = './new_pic'

# List all files in the original directory
filenames = os.listdir(ori_path)

# Filter out only .txt files
txt_files = [f for f in filenames if f.endswith('.txt') and os.path.isfile(os.path.join(ori_path, f))]

# Process each text file
for file_ in txt_files:
    # Create corresponding image file name
    img_file = file_[:-4] + '.png'  # Replace .txt with .png
    img_path = os.path.join(ori_path, img_file)  # Full image path

    # Check if the image file exists before proceeding
    if os.path.isfile(img_path):
        print(f"Processing {img_path}")

        # Open the image and convert to grayscale
        img = Image.open(img_path).convert('L')  # Convert image to grayscale (L mode)

        # Invert the grayscale image to create a negative effect
        inverted_img = ImageOps.invert(img)

        # Prepare output file name
        save_name = os.path.join(save_path, f"{file_[:-4]}_inverted.png")  # Save as PNG
        inverted_img.save(save_name)  # Save the inverted image

        # Copy the corresponding text file to the new location
        save_txt = shutil.copy(os.path.join(ori_path, file_), os.path.join(save_path, f"{file_[:-4]}_inverted.txt"))
    else:
        print(f"Image file not found: {img_path}")
