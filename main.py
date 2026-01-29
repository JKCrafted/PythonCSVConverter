import csv, os




def GetInputFile():
    while True:
        inputFile = input("Input file Directory: ")
        if os.path.exists(inputFile) and (".csv" in inputFile or ".py" in inputFile):
            return inputFile
        else:
            print("Error, inputted file directory not valid")



def ToCSV():
    inputFile = GetInputFile()
    with open(inputFile, encoding="utf-8") as file1:
        lines = file1.readlines()
        newLines = []
        linesLength = 0
        for line in lines:
            splitLines = (str(line).replace("\n", "").replace('"', '""').replace("    ", "\t")).split("\t")
            if len(splitLines) > linesLength:
                linesLength = len(splitLines)
            newLine = ""
            for splitLine in splitLines:
                if "," in splitLine:
                    splitLine = f'"{splitLine}"'
                newLine += splitLine + ","
            newLines.append(newLine)
        newLines2 = []
        for newLine2 in newLines:
            splitnewLine2 = newLine2.split(",")
            newLength = len(splitnewLine2) 
            if newLength > 0:
                for i in range(len(splitnewLine2)):
                    if len(splitnewLine2[i]) > 0:
                        if splitnewLine2[i][0] == '"':
                            if i < len(splitnewLine2):
                                if len(splitnewLine2[i+1]) > 0:
                                    if splitnewLine2[i+1][-1] == '"':
                                        newLength -= 1
            while newLength < linesLength:
                newLine2 += ","
                newLength += 1
            newLines2.append(newLine2)
        newFileName = inputFile.replace(".py", ".csv")
        with open(newFileName, "a", encoding="utf-8") as file2:
            for finalLine in newLines2:
                file2.write(f"{finalLine}\n")






def FromCSV():
    inputFile = GetInputFile()
    with open(inputFile, "r", encoding="utf-8") as file1:
        csvFile = csv.reader(file1)
        for lines in csvFile:                
            newFileName = inputFile.replace(".csv", ".py")
            with open(newFileName, "a", encoding="utf-8") as file2:
                for finalLine in lines:
                    finalLine = finalLine.replace('""', '"')
                    if finalLine == '':
                        finalLine = "\t"
                    file2.write(f"{finalLine}")
                file2.write(f"\n")
                




def Start():
    while True:
        goal = input("To CSV (1), From CSV (2): ")
        if goal == "1":
            ToCSV()
            break
        elif goal == "2":
            FromCSV()
            break
        else:
            print("Error, input not valid")








if __name__ == "__main__":
    Start()