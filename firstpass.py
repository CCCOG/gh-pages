#Run this file on the original text document first before any other python files are ran!!!!

#This script will read in the file that is listed when ran (fileIn) and output a texptext.txt file with 
#all the non-Windows formatting characters removed/replaced.
#############  This file does almost nothing now that I am encoding in utf-8. Consider removing next year ###############################


def firstFunc(fileIn, raw):
    with open(fileIn, 'r', encoding="UTF-8", errors="surrogateescape") as f:
        data = f.read()

        #Prints the "raw" data to the terminal output so you can look through it and find the marks that 
        #don't fit. (Before the replacments)
        if raw == "before-start":
            print(repr(data)[0:100000])
        elif raw =="before-end":
            print(repr(data)[100000:])

 
        data = data.replace('(NIV)', '')
        data = data.replace('NIV', '')
        data = data.replace('\t', '')
        data = data.replace('\f', '')

        #Prints the "raw" data to the terminal output so you can look through it and find the marks that 
        #don't fit.
        if raw == "after-start":
            print(repr(data)[0:100000])
        elif raw == "after-end":
            print(repr(data)[100000:])

    with open('firstpassout.txt', 'w', encoding="UTF-8", errors="surrogateescape") as f:
        f.write(data)

if __name__ == "__main__":
    fileIn = input("What is the name of the source file to use? \n>>")
    print("Would you like terminal output for the firstpass operation? ")
    raw = input("Options: before-start, before-end, after-start, after-end, none (default is none)\n>>")
    try:
        firstFunc(fileIn, raw)
    except FileNotFoundError as e:
        print(e)
        print("Possible causes for this error:")
        print("1. File name was not supplied.")
        print("2: File does not exist in the directory. It should be listed in the same folder as the firstpass.py file.")
        print("3: The file name was typed incorrectly")
        print("Please try again.")