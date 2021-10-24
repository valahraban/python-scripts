## really hacky python script to estimate the encoding of all the files in your folder with chardet and a tqdm loadbar: run at your own risk
## meant to be used while piping the output to a text file from your shell if you're working on a massive amount of files e.g.: python globchardet.py >> output.txt
## WTFPL by valahraban
import sys
import glob
import chardet
from tqdm import tqdm

for filename in tqdm(glob.glob("**/*.*", recursive=True)):
    with open(filename, 'rb') as f:
        out_name = filename
        rawdata = f.read()
        result = chardet.detect(rawdata)
        charenc = result['encoding']
        print("Encoding of " + str(filename) + " is " + str(charenc))

input("press return to exit")
