#Splits a file line by line by delimiter and saves the second half to a output file.
#Good for spliting somthing like a list of dorks and keeping the second half (suffix).
#I.E:  keywordBlah.php?cart=70 will result in just .php?cart=70

delimiter = "."
inputFile = "dork.txt"
outputFile = "dorkSuffix.txt"

with open(inputFile, 'r') as f:
    lines = f.read().splitlines()

with open(outputFile, 'w') as f:
    for line in lines:
        if delimiter in line:
            suffix = line.split(delimiter)[1]
            f.write(delimiter + suffix + "\n")
            print(delimiter + suffix)

print("[DONE - <3 MERKLE]: " + str(len(lines)) + " Items saved to, " + outputFile)
        