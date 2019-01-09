#Seth Turnage
#ASU Student
#Python program to convert json to CSV so I can use it for my market brief Alexa skill, written in C#

import csv
import json 
import os
import sys
import re
#put the local urls of the files you want to convert here
COMMENTS = True
JSON_Files_To_Be_Converted = ["JSON/symbols.json"]
Column_Names = ["slot Value", "identifier", "synonym","synonym2","synonym3"] 
Create_CSV_URL = "slots.CSV"

try:
    os.remove(Create_CSV_URL)
except OSError:
    pass

for CURRENT_FILE in range(0,JSON_Files_To_Be_Converted.__len__()):
    with open(JSON_Files_To_Be_Converted[CURRENT_FILE],'r') as json_file:
        json_loaded = json.load(json_file)
        value = ""
        identifier = ""
        synonym = ""
        synonym2 = ""
        synonym3 = ""

        with open(Create_CSV_URL, 'a') as output:
            #write column names
            output.write("slot Value,identifier,synonym,synonym2,synonym3\n")
            #write rows of data
            for index, item in enumerate(json_loaded):
                value = ""
                identifier = ""
                synonym = ""
                synonym2 = ""
                synonym3 = ""
                value = item["name"]
                if not value.strip():
                    value = "No Name"
                list_of_all_words = value.split(" ")
                #location and punctate all achromyns with periods
                #for word in list_of_all_words:
                 #   print(word)
                  #  if word.isupper() == True:
                   #     print("WE FOUND OURSELVES AN ACHRONYM")
                  #      achronym = ""
                  #      for letter in word:
                 #           achronym += letter
                #            achronym += "." 
                #        value = value.replace(word,achronym)
                #    elif "//" in word:
                #        value = value.replace(word,"")

                #get rid of parenthetical statements
                try:
                    value = value.replace(re.search(r'\(([^)]+)', value).group(1),"")
                    value = value.replace("(","")
                    value = value.replace(")","")
                except:
                    pass
                
                value = value.replace(" etn "," E.T.N. ")
 
                phrase = "Corp."
                phrase2 = "Corp " 
                if phrase in value:
                    synonym2 = value.replace("Corp.","corporation")
                elif phrase2 in value:
                    synonym2 = value.replace("Corp ","corporation")
                if phrase in value:
                    synonym3 = value.replace("Corp.","")
                elif phrase2 in value:
                    synonym3 = value.replace("Corp ","")
                phrase = "corp."
                phrase2 = "corp " 
                if phrase in value:
                    synonym2 = value.replace("corp.","corporation")
                elif phrase2 in value:
                    synonym2 = value.replace("corp ","corporation")
                if phrase in value:
                    synonym3 = value.replace("corp.","")
                elif phrase2 in value:
                    synonym3 = value.replace("corp ","")
                phrase = "corporation"
                phrase2 = "incorporated" 
                if phrase in value:
                    synonym2 = value.replace("corporation","corp.")
                elif phrase2 in value:
                    synonym2 = value.replace("incorporated","inc.")
                if phrase in value:
                    synonym3 = value.replace("corporation","")
                elif phrase2 in value:
                    synonym3 = value.replace("incorporated","")
                phrase = "inc."
                phrase2 = "inc " 
                if phrase in value:
                    synonym2 = value.replace("inc.","incorporated")
                elif phrase2 in value:
                    synonym2 = value.replace("inc ","incorporated")
                if phrase in value:
                    synonym3 = value.replace("inc.","")
                elif phrase2 in value:
                    synonym3 = value.replace("inc ","")
                phrase = "Inc."
                phrase2 = "Inc " 
                if phrase in value:
                    synonym2 = value.replace("Inc.","incorporated")
                elif phrase2 in value:
                    synonym2 = value.replace("Inc ","incorporated")
                if phrase in value:
                    synonym3 = value.replace("Inc.","")
                elif phrase2 in value:
                    synonym3 = value.replace("Inc ","")

                identifier = item["symbol"]
                identifier_letters = item["symbol"].lower()
                symbol_spoken = ""
                for letter in identifier_letters:
                    symbol_spoken += letter
                    symbol_spoken += "."
                symbol_spoken = symbol_spoken.replace("-"," dash ")
                symbol_spoken = symbol_spoken.replace("+"," plus ")
                symbol_spoken = symbol_spoken.replace("...",". dot ")                      
                synonym = symbol_spoken
               
                line = value + "," + identifier + "," + synonym + "," + synonym2 + "," + synonym3 + "\n"
                output.write(line)
