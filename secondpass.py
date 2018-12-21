# Run this file second only after the firstpass.py file is ran!!!!
# The goal of the secondpass script is to convert the firstpassout.txt file into 
# a JSON file that can be used by later scripts. 

# Globals
day = 1
total_lines_for_this_day = 1
currentLine = "Place holder"

def secondFunc(leap):
    fI = open("firstpassout.txt", "r")
    fO = open("secondpassout.json", "w")

    
    #setup the json file
    fO.write('{\n"dayText" : {\n"1" : {\n')

    def create_json_entry():
        global day
        global total_lines_for_this_day
        global currentLine
        currentLine = fI.readline()
        
        
        #print("From create_json_entry: currentLine is %r" %currentLine)
        if (currentLine == "\n" or currentLine == "' '\n"):
            # print("I found a new line. Passing")
            pass
        elif (currentLine == ""):
            day = (day + 100)# Just to make it break
        else:
            currentLine = currentLine.rstrip()
            #print(currentLine[-5:])
            #print("The currentLine var is = %r" % currentLine)
            #print("The currentLine var is = {}" .format(currentLine))
            # if (currentLine[-5:] == "Amen." or currentLine[-7:] == "Burial)" or currentLine[-5:] == "Amen!" or currentLine.endswith("Hallelujah!")):
            if (currentLine.endswith("Amen.") or currentLine.endswith("Burial)") or currentLine.endswith("Amen!") or currentLine.endswith("Hallelujah!")):
                fO.write('"line')
                fO.write(str(total_lines_for_this_day))
                fO.write('" ' + ': "'  + currentLine + '", \n')
                fO.write('"line_count')
                fO.write('"' + ': ')
                #print("Total lines for the day = %s" %total_lines_for_this_day)
                fO.write('%d' % total_lines_for_this_day)
                fO.write(' \n')
                total_lines_for_this_day = 1
                # Writes the day counter and the Json : { characters
                day = (day + 1)
                if (leap == "yes"):# leap year
                    if (day <= 366): # leap year
                        fO.write('}, \n"' + str(day) + '" : { \n')                    
                elif day <= 365:
                    fO.write('}, \n"' + str(day) + '" : { \n')
                else:
                    pass
                    
                    
                    

                total_lines_for_this_day = 1
            else:
                currentLine = currentLine.rstrip()
                fO.write('"line')
                fO.write(str(total_lines_for_this_day))
                fO.write('" ' + ': "' + currentLine + '", \n')
                total_lines_for_this_day += 1
       

    if leap == 'yes':
        while (day < 367):# leap year
            create_json_entry()
    else:
        while (day < 366):# non-leap year
             create_json_entry()

    #Finish up Json file
    fO.write(' }\n}\n}')
    fI.close()
    fO.close()

if __name__ == "__main__":
    leap = input("Is this for a leap year? (type yes or leave blank)\n>>")
    leap = leap.lower()
    try:
        secondFunc(leap)
        print("The secondpass script is complete.\n\n\n")
    except Exception as e:
        print(e)