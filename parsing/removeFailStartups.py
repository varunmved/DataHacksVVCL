fileN = open("newfile.txt", "r")
fileO = open("newfile3.txt", "w")

for line in fileN:
    if not "[]" in line:
        fileO.write(line)

