## A script you define a list of bad characters or strings in
## If your .txt file contains said strings they get removed while everything else stays the same
## Warning, I wrote this in github without any testing, write to a new filename if you fear bricking your source
## WTFPL by valahraban, rmvstr=removestring
source_file = open(input("Enter a filename to modify: "), "r")
lines = source_file.readlines()
source_file.close()
new_file = open(input("Enter a filename to output: "), "w", encoding="utf-8")
for line in lines:
    line.replace("=","") ##add one of these for every chr/str you want to remove
new_file.close()
