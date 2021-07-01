## Run this script in folder
## Script goes through .txt files located with glob and performs modifications on the entire file
## The defaults of this program are for processing .txt for use in NLP datasetting
## For use in your own batch text editing, learn to use regex and tweak the script for your needs
## Licensed: GPLv3.0 by valahraban
import sys
import re ## regex ## re.I, re.M
from re import search ## regex search if needed 
import glob
import ftfy

for filename in glob.glob("**/*.txt", recursive=True): ## if you want to do recursive mode instead which is more dangerous
#for filename in glob.glob("*.txt"): ## glob stores filenames
    with open(filename, 'r+', encoding='utf-8', errors='ignore') as f: # open files in rw-mode, iterate, skip encoding errors
        text = f.read() # modification go under this
        text = re.sub(r'( |\t)+', ' ', text) # unindent
        text = re.sub(r'(^|\n)( |\t)+', r'\1', text) # unindent
        text = ftfy.fix_text(text).replace(' …', '...').replace('…', '...').replace('\N{SOFT HYPHEN}', '').replace('\u200b', '').replace(u"\uFFFD", '') # clean up special
        text = text.replace(' ,',',').replace('---|---|---','').replace('---|---','').replace('---|','') # fix weird grammar, tables and errors
        text = re.sub('\\.{3,}', '...', text) # shorten trailing dots to ...
        text = re.sub('\\*{3,}', '***', text) # shorten trailing asterisks
        text = re.sub(r"(\b|\s)''(\b|\s)", r'\1"\2', text) # turn '' into "
        text = re.sub(r'"+', '"', text) # fix multiple quotes
        text = re.sub(r"'+", "'", text) # fix multiple quotes
        text = re.sub('(^" | "$)', '"', text, flags=re.M) # purge trailing spaces from quotes
        text = re.sub(r'https?:\/\/[^\s\)\]\}]*', '', text) # purging https before doing newlines
        text = re.sub(r'\bwww\.[a-zA-Z0-9\-\.\/\~\_]+', '', text) # purging www before doing newlines
        text = text.replace('\r\n', '\n').replace('\r', '\n') # normalize newlines
        text = text.replace('\n\n\n', '\n').replace('\n\n', '\n') # no linebreaks
        text = re.sub(r'^(epilogue.?|prologue.?)(\n|$)', "***", text, flags=re.I | re.M)
        text = re.sub('^(begin reading|insert|table of contents|title page|copyright page|dedication.?|acknowledgement.?|content.?|endnote.?)(\n|$)', "", text, flags=re.I | re.M)
        text = re.sub(r'<\|endoftext\|>', '', text)
        text = re.sub(r'^(.*)?(Yen On|Yen Press|Tor Publishing)(.*)?(\n|$)', "", text, flags=re.M) # purge undesired strings
        text = re.sub(r'^Identifiers:?(.*)?(\n|$)', "", text, flags=re.M)
        text = re.sub(r'^ISBN(.*)?(\n|$)', "", text, flags=re.M)
        f.seek(0) ## pointer at top of file
        f.write(text) ## write to file
        f.truncate() ## truncate and close, continue

input("press return to exit") # optional
