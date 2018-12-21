import json

def fourthFunc(yearOut):
    #books_of_the_bible = ['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Joshua', 'Judges', 'Ruth', '1 Samuel', '2 Samuel', '1 Kings', '2 Kings', '1 Chronicles', '2 Chronicles', 'Ezra', 'Nehemiah', 'Esther', 'Job', 'Psalm', 'Proverbs', 'Ecclesiastes', 'Song of Solomon', 'Isaiah', 'Jeremiah', 'Lamentations', 'Ezekiel', 'Daniel', 'Hosea', 'Joel', 'Amos', 'Obadiah', 'Jonah', 'Micah', 'Nahum', 'Habakkuk', 'Zephaniah', 'Haggai', 'Zechariah', 'Malachi', 'Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans', '1 Corinthians', '2 Corinthians', 'Galatians', 'Ephesians', 'Philippians', 'Colossians', '1 Thessalonians', '2 Thessalonians', '1 Timothy', '2 Timothy', 'Titus', 'Philemon', 'Hebrews', 'James', '1 Peter', '2 Peter', '1 John', '2 John', '3 John', 'Jude', 'Revelation']


    with open("thirdpassout.json") as json_file:  
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
                        line_list = data["dayText"][day]["line2"].split(" - ")
                        data["dayText"][day]["line2"] = line_list
                        # line_list = []
                        # removeWatchWord = data["dayText"][day]["line2"].replace("Watchword for the Week - ", "")
                        # line_list.append(removeWatchWord)
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
                    line_list = data["dayText"][day]["line2"].split(" - ")
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
    with open(fileNameOut, 'w') as json_out:  
        json.dump(data, json_out)


if __name__ == "__main__":
    yearOut = input("What is the year of this text? (Example: 2017)\n>>")
    
    try:
        fourthFunc(yearOut)
        print("The fourthpass script is complete.\n\n\n")
    except Exception as e:
        print(e)