#This module handles all the statistical processing for the text.

#Processes a given string (usually the text of a file) and returns word count)
def get_num_words(content):
    word_list = content.split()
    num_words = len(word_list)
    return num_words

def count_characters(content):
    characters = {}
    for character in content: #For each character in the text...
        character = character.lower() #Make sure it is lowercase.
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1 #Add one to the appropriate dictionary entry?
    return characters