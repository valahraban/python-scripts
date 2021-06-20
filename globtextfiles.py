## Run this script in folder
## Script goes through .txt files located with glob and performs modifications on the entire text
## The defaults of this program are for processing .txt for use in NLP datasetting
## WTFPL by valahraban
import sys
import re ## regex
from re import search ## regex search if needed
import glob

for filename in glob.glob('*.txt'): ## glob stores filenames
    with open(filename, 'r+', encoding='utf-8') as f: ## open files in rw-mode, iterate
        text = f.read() ## modification go under this
        text = text.replace('\n\n\n', '\n').replace('\n\n', '\n')
        f.seek(0) ## pointer at top of file
        f.write(text) ## write to file
        f.truncate() ## truncate and close, continues
