# made for datasetting, detect most common image types, output txts with same filename
# output is the folder where the script is opened
# cmd on windows threw weird errors, I probably just wrote the path wrong the first time
# WTFPL
import os

# Specify the directory where the image files are stored
dir_path = 'C:\\Datasets\\Example'

# Create a list to store the image file names
image_files = []

# Loop through the files in the directory
for file in os.listdir(dir_path):
    # Check if the file is an image file
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        # Add the file name to the image_files list
        image_files.append(file)

# Loop through the image files and create text files with their names
for file_name in image_files:
    # Remove the file extension from the name
    name_without_ext = os.path.splitext(file_name)[0]
    # Create a new text file with the image file name as its name
    with open(f"{name_without_ext}.txt", "w") as f:
        f.write(file_name)
