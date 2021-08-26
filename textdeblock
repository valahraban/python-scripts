## dead simple script that makes plain text files look less blocky, and more like prose with proper paragraphs
## by valahraban
import sys
import re ## regex ## re.I, re.M
from re import search ## regex search if needed 
import glob

for filename in glob.glob("**/*.txt", recursive=True): ## if you want to do recursive mode instead which is more dangerous
#for filename in glob.glob("*.txt"): ## glob stores filenames
    with open(filename, 'r+', encoding='utf-8', errors='ignore') as f: # open files in rw-mode, iterate
        text = f.read() # modification go under this
        text = re.sub(r'(?<![.!?"*)>]) ?$\n', ' ', text) # define limiters then deblock
        f.seek(0) ## pointer at top of file
        f.write(text) ## write to file
        f.truncate() ## truncate and close, continues

input("press return to exit")
