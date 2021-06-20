## Run this script in folder
## Script goes through every line of every .txt file and does text modifications
## The defaults of this program are for processing .txt for use in NLP datasetting
## instead of adding more lines with proxy, you can do proxy = proxy.replace().replace() until happy
## WTFPL by valahraban
import sys
import re ## regex
from re import search ## regex search if needed
import glob
import fileinput
#import argparse ## reminder to implement cli arguments

for line in fileinput.input(glob.glob('*.txt'), inplace=True): ## goes through every line of every file in glob, define actions below
    proxy = line ## preserve original lines and avoid duplication by parsing proxy variable instead
    proxy = proxy.replace('\r\n', '\n').replace('\r', '\n')
    proxy = proxy.replace('\n\n\n', '\n').replace('\n\n', '\n')
    proxy = re.sub('\\.{3,}', '...', proxy) ## substitute matched regex re.sub(pattern, replacement, string, count=0, flags=0)
    proxy = proxy.replace('<|endoftext|>','') ## remove EOT for GPT-Neo
    proxy = proxy.replace('“','"')
    proxy = proxy.replace('”','"')
    proxy = proxy.replace('’',"'")
    sys.stdout.write(proxy) ## write the modified line into file, continue
