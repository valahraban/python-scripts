## A script that calculates the average length of lines in a txt file
## Whipped up in github editor
## WTFPL by valahraban
source_file = open(input("Enter a filename to check average line length of: "), "r")
lines = source_file.readlines()
source_file.close()
total_avg = sum( map(len, lines) ) / len(lines)
total_avg = round(total_avg)
str_avg = str(total_avg)
print("The average length of lines is " + str_avg + " characters.")
input("press return to exit")
