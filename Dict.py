import json
from difflib import get_close_matches

# import data source.
data = json.load(open("./data2.json"))


# Define function to take word as input and return the meaning.
print(" संस्कृत शब्दकोश: (English to Sanskrit)")
def translate(input_word):
    word = input_word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:  # if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data:  # in case user enters words like ALPHABET
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0:
        yn = input("Did you mean %s instead? [y/n]" %get_close_matches(word,data.keys())[0])
        if yn == 'y' or yn == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'n' or yn == 'N':
            return "Sorry. The word doesn't exist in the dictionary"
        else:
            return "Invalid input. We didn't understand your query."
    else:
        return "The word doesn't exist. Please double check it."


def format_output(output, input_word):
    if type(output) == list:
        print("Tanslate:")
        for item in output:
            print(item)
    else:
        print(output)


input_word = input("Enter word :")
output = translate(input_word)
format_output(output,input_word)
