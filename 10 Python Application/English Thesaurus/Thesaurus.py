#Enter any word and this program will show its meaning
#Importing json and loading file with words and its meaning
import json
data = json.load(open("English Thesaurus\data.json"))

#Importing a module to find words close to input strings
from difflib import get_close_matches 

#Defining funnction for giving meaning of word
def find(x):
    
    #Converting text into lower case
    x = x.lower()  
    
    #Finding if the word exists
    if x in data: 
        return data[x]
    
    #Finding if the word with first letter as capital exists
    elif x.capitalize() in data: 
        return data[x.capitalize()]
    
    #Finding if the word with all capitals exists
    elif x.upper() in data: 
        return data[x.upper()]
    
    #Giving suggestion for wrong word
    #Here, 'elif len(get_close_matches(x,data.keys())) > 0' confirms if there 
    # is more than 0 similar words to the input word
    elif len(get_close_matches(x,data.keys())) > 0: 
        print("Did you mean '%s' instead ?" %get_close_matches(x,data.keys())[0])
        
        #Confirming whether the user mean't the suggested word
        a = input("Enter Y if Yes and N if No: ")
        if a == "Y" or a == "y":
            return data[get_close_matches(x,data.keys())[0]]
        elif a == "N" or a == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."

    else:
        return "The word doesn't exist. Please double check it."
    
#Taking user input
x = input("Enter word: ")

#Printing meaning
y = find(x)

#For more user friendly output
if type(y) == list:
    for item in y:
        print(item)
else:
    print(y)

