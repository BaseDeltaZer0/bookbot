#This module handles all the statistical processing for the text.

#Processes a given string (usually the text of a file) and returns word count)
def get_num_words(content):
    word_list = content.split()
    num_words = len(word_list)
    return num_words