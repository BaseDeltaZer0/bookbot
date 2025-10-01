#Importing functions from Stats
from stats import get_num_words #Takes string dump and slices it to get wordcount.
from stats import count_characters #Takes string dump and creates a dictionary of character:values
from stats import sort_characters #Takes a dictionary of character:values and converts it into a sorted list of dictionaries containing character and value

import sys

if len(sys.argv) != 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

source = sys.argv[1]

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

def print_report(source,num_words,char_sort):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {source}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in char_sort:
        if not char["Character"].isalpha(): continue
        print (f"{char["Character"]}: {char["Num"]}")
    print("============= END ===============")

main()