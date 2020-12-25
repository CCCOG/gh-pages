import json

#Run this file third after firstpass.py and secondpass.py has been ran!!!

def thirdFunc():
    days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    with open("secondpassout.json", encoding='utf-8-sig') as json_file:  
        data = json.load(json_file)


    #Lists every day object
    for day in data["dayText"]:
        #Lists every line in the day object
        for line in data["dayText"][day]:
            #Lists every day name from the days_of_the_week list
            for day_name in days_of_the_week:
                #Tries to match each day name to the first 10 letters of the line
                try:
                    #This will select a line that starts with a day but not if it's an 8 line
                    if day_name in data["dayText"][day][line][:10] and data["dayText"][day]["line_count"] != 8:
                        split_line = data["dayText"][day][line]
                        split_line = split_line.split(' — ')
                        data["dayText"][day][line] = split_line.pop(0)

                        #split_line is currently holding the verses from the date line in a list
                        split_line = split_line[0].split("; ")

                        #line_number is getting the line number of the next line. Used to get the 
                        #next set of verses to add to a full verse list. 
                        line_number = int(line[-1]) + 1

                        # creating a line name variable to access the next line
                        next_line_number = line[:4] + str(line_number)
                        
                        # next_line is the text from the line below the date line
                        next_line = data["dayText"][day][next_line_number]
                        next_line = next_line.split("; ")
                        next_line = split_line + next_line
                      
                        next_line_corrected = []
                        for verse in next_line:
                            if "\u2013" in verse:
                                fixed_verse = verse.replace("\u2013", "-")
                                next_line_corrected.append(fixed_verse)
                            else:
                                next_line_corrected.append(verse)

                        
                        # This is adding the full (split) verse list to the line below the date line
                        data["dayText"][day][next_line_number] = next_line_corrected

                    # This should only pick up and work on the eight line days   
                    elif day_name in data["dayText"][day][line][:10]:
                        print("I'm on %s day in the elis condition" % (data["dayText"][day][line]))

                        # This is handling the date line and verses
                        split_line = data["dayText"][day][line]
                        split_line = split_line.split(' — ')
                        date_list = []
                        date_list.append(split_line.pop(0))         
                        verses_to_split = split_line[0]
                        verses_to_split = verses_to_split.split("; ")

                        verses_to_split_corrected = []
                        for verse in next_line:
                            if "\u2013" in verse:
                                fixed_verse = verse.replace("\u2013", "-")
                                verses_to_split_corrected.append(fixed_verse)
                            else:
                                verses_to_split_corrected.append(verse)

                        data["dayText"][day][line] = date_list + verses_to_split_corrected

                        # Splitting the special verse lines
                        split_line = data["dayText"][day]["line4"]
                        split_line = split_line.split(' — ')
                        data["dayText"][day]["line4"] = split_line.pop(0)

                        #split_line is currently holding the verses from the date line in a list
                        split_line = split_line[0].split("; ")

                        # creating a line name variable to access the next line
                        next_line_number = "line5"

                        # next_line is the text from the line below the date line
                        next_line = data["dayText"][day][next_line_number]
                        next_line = next_line.split("; ")

                        next_line_corrected = []
                        for verse in next_line:
                            if "\u2013" in verse:
                                fixed_verse = verse.replace("\u2013", "-")
                                next_line_corrected.append(fixed_verse)
                            else:
                                next_line_corrected.append(verse)

                        next_line = split_line + next_line

                        # This is adding the full (split) verse list to the line below the date line
                        data["dayText"][day][next_line_number] = next_line_corrected
                    
                
                except TypeError:
                    pass

                try:
                    #This will go back to a 9 line day and handle the special text and verses
                    if day_name in data["dayText"][day][line][:10] and data["dayText"][day]["line_count"] == 9:
                        split_line = data["dayText"][day]["line5"]

                        if ' — ' in split_line:
                            split_line = split_line.split(' — ')
                            data["dayText"][day]["line5"] = split_line.pop(0)

                        # creating a line name variable to access the next line
                        next_line_number = "line6"

                        # next_line is the text from the line below the date line
                        next_line = data["dayText"][day][next_line_number]
                        next_line = next_line.split("; ")
                        split_line = split_line[0].split("; ")
                        next_line = split_line + next_line

                        next_line_corrected = []
                        for verse in next_line:
                            if "\u2013" in verse:
                                fixed_verse = verse.replace("\u2013", "-")
                                next_line_corrected.append(fixed_verse)
                            else:
                                next_line_corrected.append(verse)

                        # This is adding the full (split) verse list to the line below the date line
                        data["dayText"][day][next_line_number] = next_line_corrected

                except TypeError:
                    pass

    with open("thirdpassout.json", 'w', encoding='utf-8-sig') as json_out:  
        json.dump(data, json_out)

if __name__ == "__main__":
    try:
        thirdFunc()
        print("The thirdpass script is complete.\n\n\n")
    except Exception as e:
        print("There was an error: ")
        print(e)
