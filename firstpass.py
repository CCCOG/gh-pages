#Run this file on the origonal text document first before any other python files are ran!!!!

#This script will read in the file that is listed when ran (fileIn) and output a texptext.txt file with 
#all the non-Windows formatting characters removed/replaced.


def firstFunc(fileIn, raw):
    with open(fileIn, 'r', encoding="ascii", errors="surrogateescape") as f:
        data = f.read()

        #Prints the "raw" data to the terminal output so you can look through it and find the marks that 
        #don't fit. (Before the replacments)
        if raw == "before-start":
            print(repr(data)[0:100000])
        elif raw =="before-end":
            print(repr(data)[100000:])

        #If a new goofy character is found, run this script on the file and look in the terminal output
        #for something like "\udce2". Then go to the text for that day and try to understand what the 
        #character was supposed to represent and add that "replace" code like below. 
        
        
        #data = data.replace('\"', '\\"')
        #data = data.replace('\udce2\udc80\udc94', "-")
        #data = data.replace('\udce2\udc80\udc93', "-")
        #data = data.replace('\udce2\udc80\udc9c', '\\"')
        #data = data.replace('\udce2\udc80\udc9d', '\\"')
        #data = data.replace('\udce2\udc80\udc99', "'")
        #data = data.replace('\udcc2\udca0', ' ')
        #data = data.replace('\udce2\udc80\udca8', '')#took out space
        #data = data.replace('\udce2\udc80\udca0', '')
        #data = data.replace('\udce2\udc80\udc98', "'")
        #data = data.replace('\udcef\udcbf\udcbd', "-")
        data = data.replace('(NIV)', '')
        data = data.replace('\t', '')
        data = data.replace('\f', '')
        data = data.replace('\udc96', '-')
        data = data.replace('\udc97', '-')
        data = data.replace('\udc93', '\\"')
        data = data.replace('\udc94', '\\"')
        data = data.replace('\udc92', "'")
        data = data.replace('\udc86', "")
        data = data.replace('\udc91', "'")
        
        #Remove the next two when done - This allows you to search the output text for "\" and find 
        #the offending markings
        # data = data.replace('\n', '')
        # data = data.replace("\'", '')

        #Prints the "raw" data to the terminal output so you can look through it and find the marks that 
        #don't fit.
        if raw == "after-start":
            print(repr(data)[0:100000])
        elif raw == "after-end":
            print(repr(data)[100000:])

    with open('firstpassout.txt', 'w', encoding="ascii", errors="surrogateescape") as f:
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