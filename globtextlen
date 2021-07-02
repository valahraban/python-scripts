# check the average length of lines in multiple text files using glob
# WTFPL by valahraban
import sys
import glob

for filename in glob.glob("**/*.txt", recursive=True):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        out_name = filename
        lines = f.readlines()
        total_avg = sum( map(len, lines) ) / len(lines)
        total_avg = round(total_avg)
        str_avg = str(total_avg)
        print("AVG length of lines in " + out_name + " is " + str_avg + " characters")

input("press return to exit")
