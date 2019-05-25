import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word= word.lower()
    if word in data.keys():
        return data[word]
    elif len(get_close_matches(word, data.keys())) >0 :
        yn= input("Did you mean {}, if yes type 'Y' else type 'N':  ".format(get_close_matches(word, data.keys())[0]))
        if yn== "Y":
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return "The word does not exists. please recheck it "
    else:
        return "The word does not exists. please recheck it "


word = input("Enter Word: ")

print(translate(word))
