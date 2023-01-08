import json
from difflib import get_close_matches


def word_search(dict, word):
    word = word.lower()
    how_much = 1
    cutoff = 0.50
    if word in dict:
        return dict[word]
    elif word.title() in dict:
        return dict[word.title()]
    elif word.upper() in dict:
        return dict[word.upper()]
    elif len(get_close_matches(word, dict, how_much, cutoff)) > 0:
        action = input("Did you mean %s instead?  [y or n]: " % get_close_matches(word, dict.keys())[0])
        if action.lower() == 'y':
            return dict[get_close_matches(word, dict.keys())[0]]
        elif action.lower() == 'n':
            return ("The word doesn't exist, yet.")
        else:
            return ("We don't understand your entry. Apologies.")


def output(word_user):
    # Output meaning of the word
    if type(word_user) == list:
        for item in word_user:
            print("-", item)
    else:
        print("-", word_user)


def main():
    # Opening dictionary
    dict = json.load(open("data.json"))
    # Input from user
    word_user = input("Enter a word: ")

    word_output = word_search(dict, word_user)

    output(word_output)


main()
