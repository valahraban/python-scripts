## Open this script in a folder with .txt files and use Powershell if on Windows
## This script creates or overwrites a file named TOC.txt that contains the name of every .txt file in the folder
## No more comments needed that's literally all this script does
## made by valahraban, WTFPL
import glob

f = open("TOC.txt", "w", encoding="utf-8")
for file in glob.glob("*.txt"):
    if not file == "TOC.txt":
        f.write(file + "\n")
f.close()
