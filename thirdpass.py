import json

#Run this file third after firstpass.py and secondpass.py has been ran!!!

#sourceFile should = ft2017.json
def thirdFunc():
    days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    with open("secondpassout.json") as json_file:  
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
                        print("I'm on %s day" % (data["dayText"][day][line]))
                        split_line = data["dayText"][day][line]
                        split_line = split_line.split(' - ')
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
                        # This is adding the full (split) verse list to the line below the date line
                        data["dayText"][day][next_line_number] = next_line

                    # This should only pick up and work on the eight line days   
                    elif day_name in data["dayText"][day][line][:10]:
                        # This is handling the date line and verses
                        split_line = data["dayText"][day][line]
                        split_line = split_line.split(' - ')
                        date_list = []
                        date_list.append(split_line.pop(0))         
                        verses_to_split = split_line[0]
                        verses_to_split = verses_to_split.split("; ")
                        data["dayText"][day][line] = date_list + verses_to_split

                        # Splitting the special verse lines
                        split_line = data["dayText"][day]["line4"]
                        split_line = split_line.split(' - ')
                        data["dayText"][day]["line4"] = split_line.pop(0)

                        #split_line is currently holding the verses from the date line in a list
                        split_line = split_line[0].split("; ")

                        # creating a line name variable to access the next line
                        next_line_number = "line5"
                        # next_line is the text from the line below the date line
                        next_line = data["dayText"][day][next_line_number]
                        next_line = next_line.split("; ")
                        next_line = split_line + next_line
                        # This is adding the full (split) verse list to the line below the date line
                        data["dayText"][day][next_line_number] = next_line
                    
                
                except TypeError:
                    pass

                try:
                    #This will go back to a 9 line day and handle the special text and verses
                    if day_name in data["dayText"][day][line][:10] and data["dayText"][day]["line_count"] == 9:
                        split_line = data["dayText"][day]["line5"]
                        split_line = split_line.split(' - ')
                        data["dayText"][day]["line5"] = split_line.pop(0)

                        #split_line is currently holding the verses from the date line in a list
                        split_line = split_line[0].split("; ")

                        # creating a line name variable to access the next line
                        next_line_number = "line6"
                        # next_line is the text from the line below the date line
                        next_line = data["dayText"][day][next_line_number]
                        next_line = next_line.split("; ")
                        next_line = split_line + next_line
                        # This is adding the full (split) verse list to the line below the date line
                        data["dayText"][day][next_line_number] = next_line

                except TypeError:
                    pass

    with open("thirdpassout.json", 'w') as json_out:  
        json.dump(data, json_out)

if __name__ == "__main__":
    try:
        thirdFunc()
        print("The thirdpass script is complete.\n\n\n")
    except Exception as e:
        print("There was an error: ")
        print(e)
