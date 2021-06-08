## A script for replacing strings of any size
## It works now, just don't try to get too clever, the placeholder variable in for loop is required
## WTFPL by valahraban, rmvstr=removestring
source_file = open(input("Enter a filename to modify: "), "r")
lines = source_file.readlines()
source_file.close()
new_file = open(input("Enter a filename to output: "), "w", encoding="utf-8")
for line in lines: ##repeat with new strings for every string you want replaced, replacer can replace itself
    replacer = line.replace("=","") 
    new_file.write(replacer)
new_file.close()
