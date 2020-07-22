import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(words):
    words = words.lower()
    if words in data:
        return data[words]
    elif len(get_close_matches(words, data.keys())) > 0:
        yn = input("did you mean %s instead? Enter Y if Yes and N if No: " % get_close_matches(words, data.keys())[0])
        if yn == 'Y'.lower():
            return data[get_close_matches(words, data.keys())[0]]
        elif yn == 'N'.lower():
            return "The word does not exist"
        else:
            return "Invalid Input"
    else:
        return "The word does not exist"

word = input("Enter a Word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)