#Importing functions from Stats
from stats import get_num_words #Takes string dump and slices it to get wordcount.
from stats import count_characters
from stats import sort_characters

source = "books/frankenstein.txt"

#Entry function, runs get_book_text, calls necessary processing, and prints results.
def main():
    content = (get_book_text(source))
    num_words = get_num_words(content)
    chardict = count_characters(content)
    char_sort = sort_characters(chardict)
    print_report(source,num_words,char_sort)
    
#Takes the file from the address specified in main, converts it to a string, and returns it.
def get_book_text(file_path): #Takes a file path as input...
    with open(file_path, "r", encoding="utf-8") as f: #Opens it...
        content = f.read() #Returns the contents as a string.
        return (content)

def print_report(content,num_words,char_sort):
    ##Fancy formatting goes here.
    print("Anyone home?")
    for char in char_sort:
        if not char["Character"].isalpha(): continue
        print (f"{char["Character"]}: {char["Num"]}")

main()