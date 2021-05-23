## A script you define a list of bad strings into
## If your .txt file contains a line with any of the bad strings said line gets Deleted
## WTFPL by valahraban
source_file = open(input("Enter a filename to modify: "), "r")
lines = source_file.readlines()
source_file.close()
bad_strings = ['Sample','Example']

new_file = open(input("Enter a filename to output: "), "w", encoding="utf-8")
for line in lines:
    if not any(bad_string in line for bad_string in bad_strings):
            new_file.write(line)
new_file.close()
