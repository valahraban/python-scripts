## Run this script in folder
## Script goes through .txt files located with glob and performs modifications on the entire file
## The defaults of this program are for processing .txt for use in NLP datasetting
## For use in your own batch text editing, learn to use regex and tweak the script for your needs
## Licensed: GPLv3.0 by valahraban
import sys
import io ## OS compatibility, universal newlines
import re ## regex ## flags=re.I, re.M
import glob
import ftfy

for filename in glob.glob("**/*.txt", recursive=True): ## if you want to do recursive mode instead which is more dangerous
    with io.open(filename, 'r+', newline='\n', encoding='utf-8', errors='ignore') as f: # open files in rw-mode, iterate, skip encoding errors
        text = f.read() # modification go under this
        text = re.sub(r'(\t)?(Story|Storylink|Category|Genre|Author|Authorlink|Last updated|Words|Rating|Status|Content|Source|Summary|A/N):.*$', '', text, flags=re.M) # example AO3 cleaner

        text = ftfy.fix_text(text).replace(' …', '...').replace('… ', '... ').replace('…', '...').replace('\N{SOFT HYPHEN}', '').replace('\u200b', '').replace(u"\uFFFD", '').replace(u"\u009D", '').replace(u"\u0081", '') # cleanup unicode special
        text = text.replace('\r\n', '\n').replace('\r', '\n') # normalize newlines | final steps
        text = re.sub(r'\n+', '\n', text, flags=re.M) # no extra linebreaks
        text = re.sub('\n\Z','', text) # no linebreak at end-of-file
        f.seek(0) # pointer at top of file
        f.write(text) # write to file
        f.truncate() # truncate and close, continue

input("press return to exit") # optional, giving the script output so you know it finishes interpreting
