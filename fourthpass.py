import json

def fourthFunc(yearOut):
    with open("thirdpassout.json", 'r', encoding='utf-8-sig') as json_file:  
        data = json.load(json_file)

    def split_five_entires():

        #Lists every day object
        for day in data["dayText"]:

            #Lists every line for that day
            for line in data["dayText"][day]:
                if data["dayText"][day][line] == 5:
                    line_list = []
                    line_list.append(data["dayText"][day]["line1"])
                    data["dayText"][day]["line1"] = line_list
                    line_list = []
                    line_list.append(data["dayText"][day]["line3"])
                    data["dayText"][day]["line3"] = line_list
                    line_list = []
                    line_list.append(data["dayText"][day]["line4"])
                    data["dayText"][day]["line4"] = line_list
                    line_list = []
                    line_list.append(data["dayText"][day]["line5"])
                    data["dayText"][day]["line5"] = line_list
                

    def split_six_entires():

        #Lists every day object
        for day in data["dayText"]:

            #Lists every line for that day
            for line in data["dayText"][day]:
                if data["dayText"][day][line] == 6:
                    line_list = []
                    line_list.append(data["dayText"][day]["line1"])
                    data["dayText"][day]["line1"] = line_list
                    line_list = []
                    line_list.append(data["dayText"][day]["line2"])
                    data["dayText"][day]["line2"] = line_list
                    line_list = []
                    line_list.append(data["dayText"][day]["line4"])
                    data["dayText"][day]["line4"] = line_list
                    line_list = []
                    line_list.append(data["dayText"][day]["line5"])
                    data["dayText"][day]["line5"] = line_list
                    line_list = []
                    line_list.append(data["dayText"][day]["line6"])
                    data["dayText"][day]["line6"] = line_list



    def split_seven_entires():

        #Lists every day object
        for day in data["dayText"]:

            #Lists every line for that day
            for line in data["dayText"][day]:
                if data["dayText"][day][line] == 7:
                    line_list = []
                    line_list.append(data["dayText"][day]["line1"])
                    data["dayText"][day]["line1"] = line_list

                    if "Watchword" in data["dayText"][day]["line2"]:
                        line_list = data["dayText"][day]["line2"].split(" — ")
                        data["dayText"][day]["line2"] = line_list

                    data["dayText"][day]["line2"] = line_list
                    line_list = []
                    line_list.append(data["dayText"][day]["line3"])
                    data["dayText"][day]["line3"] = line_list
                    line_list = []
                    line_list.append(data["dayText"][day]["line5"])
                    data["dayText"][day]["line5"] = line_list
                    line_list = []
                    line_list.append(data["dayText"][day]["line6"])
                    data["dayText"][day]["line6"] = line_list
                    line_list = []
                    line_list.append(data["dayText"][day]["line7"])
                    data["dayText"][day]["line7"] = line_list

    def split_eight_entires():

        #Lists every day object
        for day in data["dayText"]:

            #Lists every line for that day
            for line in data["dayText"][day]:
                if data["dayText"][day][line] == 8:
                    line_list = []
                    line_list.append(data["dayText"][day]["line1"])
                    data["dayText"][day]["line1"] = line_list
                    line_list = []
                    line_list = data["dayText"][day]["line2"].split(" - ")
                    data["dayText"][day]["line2"] = line_list
                    line_list = []
                    line_list.append(data["dayText"][day]["line4"])
                    data["dayText"][day]["line4"] = line_list
                    line_list = []
                    line_list.append(data["dayText"][day]["line6"])
                    data["dayText"][day]["line6"] = line_list
                    line_list = []
                    line_list.append(data["dayText"][day]["line7"])
                    data["dayText"][day]["line7"] = line_list
                    line_list = []
                    line_list.append(data["dayText"][day]["line8"])
                    data["dayText"][day]["line8"] = line_list

    def split_nine_entires():

        #Lists every day object
        for day in data["dayText"]:
            
            #Lists every line for that day
            for line in data["dayText"][day]:
                if data["dayText"][day][line] == 9:
                    line_list = []
                    line_list.append(data["dayText"][day]["line1"])
                    data["dayText"][day]["line1"] = line_list
                    line_list = []
                    line_list = data["dayText"][day]["line2"].split(" — ")
                    data["dayText"][day]["line2"] = line_list
                    line_list = []
                    line_list.append(data["dayText"][day]["line3"])
                    data["dayText"][day]["line3"] = line_list
                    line_list = []
                    line_list.append(data["dayText"][day]["line5"])
                    data["dayText"][day]["line5"] = line_list
                    line_list = []
                    line_list.append(data["dayText"][day]["line7"])
                    data["dayText"][day]["line7"] = line_list
                    line_list = []
                    line_list.append(data["dayText"][day]["line8"])
                    data["dayText"][day]["line8"] = line_list
                    line_list = []
                    line_list.append(data["dayText"][day]["line9"])
                    data["dayText"][day]["line9"] = line_list


    split_five_entires()
    split_six_entires()
    split_seven_entires()
    split_eight_entires()
    split_nine_entires()

    # Writes the JSON to file
    fileNameOut = "final%s.json" % yearOut
    with open(fileNameOut, 'w', encoding='utf-8-sig') as json_out:  
        json.dump(data, json_out)


if __name__ == "__main__":
    yearOut = input("What is the year of this text? (Example: 2017)\n>>")
    
    try:
        fourthFunc(yearOut)
        print("The fourthpass script is complete.\n\n\n")
    except Exception as e:
        print(e)