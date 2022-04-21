## Run this script in folder
## Example script how to use tqdm in a script with glob
## In theory this script should guess what encoding your text file is using
## In practice it's extremely hard to guess what encoding a text file is using, if it's even using a single character encoding

## do whatever you want by valahraban
import sys
import glob
import chardet
from tqdm import tqdm

for filename in tqdm(glob.glob("**/*.txt", recursive=True)):
    with open(filename, 'rb') as f:
        out_name = filename
        rawdata = f.read()
        result = chardet.detect(rawdata)
        charenc = result['encoding']
        print("Encoding of " + str(filename) + " is " + str(charenc))

input("press return to exit")
