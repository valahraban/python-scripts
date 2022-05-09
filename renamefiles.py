# Requires a folder of sorted images and a sorted text file full of new names
# Goes through filenames in alphanumeric order and the text file from the top, renaming files
# Meant to be used with .png images, replace file extension with whatever you need
# I'm pretty sure a couple of lines could be shortened to names = f.read().splitlines() but I'm not changing that until further testing
# WTFPL by valahraban
import os
folder = r'C:/Users/valahraban/Test/' # windows, this is your folder with images
count = 0 # index starts at 0, needed to apply the new name from .txt list
f = open('names.txt', 'r') # names.txt is assumed to be in same folder with your script
names = f.readlines()
names2 = [i.strip('\n') for i in names] # removes leftover \n characters carried over from my .txt file
for filename in os.listdir(folder): # listdir reads filenames in the target folder, assumes alphanumeric order
    source = folder + filename # original filename, mine were numbers from 0.png to 999.png 
    newname = folder + names2[count] + ".png" # new filenames, these must be sorted correctly starting at the top to suit your needs
    os.rename(source, newname)
    count += 1 # iterate
f.close()
